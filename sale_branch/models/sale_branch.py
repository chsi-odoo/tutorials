from odoo import models, fields, api


class SaleBranch(models.Model):
    _name = 'sale.branch'
    _description = "Branch for sales"

    _sql_constraints = [
        ('name_unique', 'UNIQUE(name)', "Name must be unique"),
        ('code_unique', 'UNIQUE(code)', "Code must be unique"),
    ]

    name = fields.Char(required=True)
    sequence_id = fields.Many2one("ir.sequence")
    code = fields.Char(required=True, readonly=True)

    @api.model
    def create(self, vals):
        # self.ensure_one()

        created_sequence = self.env['ir.sequence'].create([{
            'name': vals['name'],
            'code': vals['code'],
        }])
        vals['sequence_id'] = created_sequence.id

        return super().create(vals)
