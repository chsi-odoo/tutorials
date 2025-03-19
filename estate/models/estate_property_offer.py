from __future__ import annotations

import datetime
from datetime import timedelta
from typing import Collection

from .estate_property import *
from odoo import api, models, fields


class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"

    _description = "Estate Property Offers _"

    _sql_constraints = [
        ('check_price', 'CHECK(price > 0)', 'Offer price must be positive'),
    ]

    _order = "price desc"

    price = fields.Float()
    status = fields.Selection(selection=[('accepted', 'Accepted'), ('refused', 'Refused')], copy=False,
                              inverse='_invert_status')
    partner_id = fields.Many2one("res.partner", required=True, string="Partner")
    property_id = fields.Many2one("estate.property", required=True, string="Property")
    validity = fields.Integer(default=7, string="Validity (days)", inverse='_invert_validity')
    date_deadline = fields.Date(compute='_compute_date_deadline', inverse='_invert_date_deadline', string="Deadline")
    property_type_id = fields.Many2one(related="property_id.property_type_id", store=True)

    # i hope there are proper types
    def _get_create_date(self) -> datetime.date:
        if not self.create_date:
            return datetime.date.today()
        return self.create_date.date()

    @api.depends('create_date', 'validity')
    def _compute_date_deadline(self: Collection[EstatePropertyOffer]):
        for record in self:
            record.date_deadline = record._get_create_date() + timedelta(days=record.validity)

    def _invert_date_deadline(self: Collection[EstatePropertyOffer]):
        for record in self:
            delta: timedelta = record.date_deadline - record._get_create_date()
            record.validity = delta.days

    def _invert_validity(self: Collection[EstatePropertyOffer]):
        for record in self:
            record.date_deadline = record._get_create_date() + timedelta(days=record.validity)

    def action_accept(self: Collection[EstatePropertyOffer]):
        for record in self:
            record.status = 'accepted'

        return True

    def action_refuse(self: Collection[EstatePropertyOffer]):
        for record in self:
            record.status = 'refused'

        return True

    def _invert_status(self):
        for record in self:
            estate_property: EstateProperty = record.property_id
            print(estate_property)
            offer_siblings = estate_property.offer_ids
            print(record)
            is_selected = record.status == 'accepted'
            is_parent_status_non_terminal = not (estate_property.state == 'accepted' or estate_property.state == 'cancelled')

            if is_selected:
                for sibling in filter(lambda x: x.status and x != record, offer_siblings):
                    sibling.status = 'refused'

                estate_property.selling_price = record.price
                estate_property.buyer_id = record.partner_id
                if is_parent_status_non_terminal:
                    estate_property.state = 'offer_accepted'


            else:
                # the inverse function will be triggered by other siblings when their statuses are set to accepted
                # and our offer is currently accepted
                any_accepted_siblings = any(x.status == 'accepted' and x != record for x in offer_siblings)
                if not any_accepted_siblings:
                    estate_property.selling_price = None
                    estate_property.buyer_id = None

                    #maybe disallow changing offer statuses after property has been sold?
                    if is_parent_status_non_terminal:
                        estate_property.state = 'offer_received'