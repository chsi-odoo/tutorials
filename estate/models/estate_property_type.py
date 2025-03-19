from odoo import models, fields

class EstatePropertyType(models.Model):
    _name = 'estate.property.type'

    _description = 'Estate Property Types _'

    _sql_constraints = [
        ('name_unique','UNIQUE(name)','Type name must be unique'),
    ]

    name = fields.Char(required=True)


