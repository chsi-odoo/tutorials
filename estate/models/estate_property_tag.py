from odoo import models, fields

class EstatePropertyTag(models.Model):
    _name = "estate.property.tag"

    _description = "Estate Property Tags _"

    _sql_constraints = [
        ('name_unique','UNIQUE(name)','Tag name must be unique'),
    ]

    _order = "name asc"

    name = fields.Char(required=True)
    color = fields.Integer()