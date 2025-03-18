from odoo import models, fields

class EstatePropertyTag(models.Model):
    _name = "estate.property.tag"

    _description = "Estate Property Tags _"

    name = fields.Char(required=True)