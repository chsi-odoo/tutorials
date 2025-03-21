from odoo import models, fields, api


class SaleBranch(models.Model):
    _name = 'sale.branch'
    _description = "Branch for sales"

    name = fields.Char(required=True)
    sequence_id  = fields.Many2one("ir.sequence")
    code = fields.Char(required=True)

    @api.model
    def create(self, vals):
        # self.ensure_one()

        created_sequence = self.env['ir.sequence'].create([{
            'name': vals['name'],
            'code': vals['code'],
        }])
        vals['sequence_id'] = created_sequence.id

        return super().create(vals)