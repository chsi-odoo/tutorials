from odoo import models, fields, api, _


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    branch_id = fields.Many2one('sale.branch')

    @api.model
    def create(self, vals):

        # vals['name'] = self.env['ir.sequence'].with_company(vals.get('company_id')).next_by_code(
        #     'sale.order', sequence_date=seq_date) or _("New")


        branch = self.env['sale.branch'].browse(vals['branch_id'])
        sequence_code = branch.code or 'sale.order'
        sequence_id = self.env['ir.sequence'].next_by_code(sequence_code) or _("New")

        vals['name'] = f'{branch.code}{sequence_id}' if branch else sequence_id


        return super().create(vals)