from __future__ import annotations
from odoo import api, models, fields
from datetime import timedelta
from dateutil.relativedelta import relativedelta
from typing import Collection, Iterable

from odoo.exceptions import UserError, ValidationError
from .estate_property_offer import EstatePropertyOffer


# this isnt working lmao

class EstateProperty(models.Model):
    _name = 'estate.property'

    _description = "Estate property"

    _sql_constraints = [
        ('check_expected_price', 'CHECK(expected_price > 0)','Expected price must be positive'),
        ('check_selling_price', 'CHECK(selling_price >= 0)','Selling price must be non-negative'),
    ]

    _order = "id desc"

    active = fields.Boolean(default=True)
    state = fields.Selection(
        string='Status',
        default='new',
        required=True,
        copy=False,
        selection=[('new', 'New'), ('offer_received', 'Offer Received'), ('offer_accepted', 'Offer Accepted'), ('sold','Sold'),('cancelled','Cancelled')],)
    name = fields.Char(required=True, help='lmao', string="Title")
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date(copy=False, default=lambda _: fields.Datetime.today() + relativedelta(months=+3), string="Available From")
    expected_price = fields.Float(required=True)
    selling_price = fields.Float(readonly=True, copy=False)
    bedrooms = fields.Integer(default=2)
    living_area = fields.Integer(string="Living Area (sqm)")
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(
        selection=[('north', 'North'), ('south', 'South')]
    )
    property_type_id = fields.Many2one("estate.property.type", string="Property Type")
    salesperson_id = fields.Many2one("res.users", string ="Salesperson", default=lambda self: self.env.user)
    buyer_id = fields.Many2one("res.partner", string="Buyer", copy=False)
    tag_ids = fields.Many2many("estate.property.tag", string="Tags")
    offer_ids = fields.One2many("estate.property.offer", "property_id", string="Offers")
    total_area = fields.Float(compute='_compute_total_area')
    best_price = fields.Float(compute='_compute_best_price', string='Best Offer')

    @api.depends("living_area","garden_area")
    def _compute_total_area(self: Collection[EstateProperty]):
        for record in self:
            record.total_area = record.living_area + record.garden_area

    @api.depends("offer_ids")
    def _compute_best_price(self: Collection[EstateProperty]):
        for record in self:
            # prices: Collection[float] = record.offer_ids.mapped('price')
            record.best_price = min(record.offer_ids.mapped('price'), default=None)

    @api.onchange("garden")
    def _onchange_garden(self):
        isGardenSelected = self.garden

        if isGardenSelected:
            self.garden_area = 10
            self.garden_orientation = 'north'
        else:
            self.garden_area = 0
            self.garden_orientation = None

    def action_set_state_cancelled(self: Collection[EstateProperty]):
        for record in self:
            record.state = 'cancelled'
        return True

    def action_set_state_sold(self: Collection[EstateProperty]):
        for record in self:
            is_cancelled = record.state == 'cancelled'
            if is_cancelled:
                raise UserError('Canceled properties cannot be sold')

            record.state = 'sold'

    @api.constrains("selling_price")
    def _check_selling_price(self: Collection[EstateProperty]):
        for record in self:
            threshold = record.expected_price * 0.9 or 0
            offer_statuses: Collection[str] = record.offer_ids.mapped('status')
            is_offer_being_accepted = any(status == 'accepted' for status in offer_statuses)
            if is_offer_being_accepted and record.selling_price < threshold:
                raise ValidationError("The selling price is (message is too long...)")

    @api.ondelete(at_uninstall=False)
    def _unlink_if_cancellable_state(self: Collection[EstateProperty]):
        if any(record.state not in ('new', 'cancelled') for record in self):
            raise UserError('No cancelling plzz')
