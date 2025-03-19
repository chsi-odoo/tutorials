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

    price = fields.Float()
    status = fields.Selection(selection=[('accepted', 'Accepted'), ('refused', 'Refused')], copy=False,
                              inverse='_invert_status')
    partner_id = fields.Many2one("res.partner", required=True, string="Partner")
    property_id = fields.Many2one("estate.property", required=True, string="Property")
    validity = fields.Integer(default=7, string="Validity (days)", inverse='_invert_validity')
    date_deadline = fields.Date(compute='_compute_date_deadline', inverse='_invert_date_deadline', string="Deadline")

    @api.depends('create_date', 'validity')
    def _compute_date_deadline(self: Collection[EstatePropertyOffer]):
        for record in self:
            record.date_deadline = (record.create_date or datetime.date.today()) + timedelta(days=record.validity)

    def _invert_date_deadline(self: Collection[EstatePropertyOffer]):
        for record in self:
            delta: timedelta = record.date_deadline - (record.create_date or datetime.date.today())
            record.validity = delta.days

    def _invert_validity(self: Collection[EstatePropertyOffer]):
        for record in self:
            record.date_deadline = (record.create_date or datetime.date.today()) + timedelta(days=record.validity)

    def action_accept(self: Collection[EstatePropertyOffer]):
        for record in self:
            record.status = 'accepted'

        return True

    def action_refuse(self: Collection[EstatePropertyOffer]):
        for record in self:
            record.status = 'refused'

        return True

    def _invert_status(self):
        estate_property = self.property_id
        offer_siblings = estate_property.offer_ids

        is_selected = self.status == 'accepted'
        if is_selected:
            for sibling in filter(lambda x: x.status and x != self, offer_siblings):
                sibling.status = 'refused'

            estate_property.selling_price = self.price
            estate_property.buyer_id = self.partner_id

        else:
            # the inverse function will be triggered by other siblings when their statuses are set to accepted
            # and our offer is currently accepted
            any_accepted_siblings = any(x.status == 'accepted' and x != self for x in offer_siblings)
            if not any_accepted_siblings:
                estate_property.selling_price = None
                estate_property.buyer_id = None
