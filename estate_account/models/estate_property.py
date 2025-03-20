from odoo import models, Command


class EstateProperty(models.Model):
    _inherit = "estate.property"

    # maybe we dont have to copy and use the implementation directly and can instead use some default methods define somewhere?
    # TODO try improve this
    def _get_default_journal(self):
        # journal_type = self.env.context.get('journal_type', 'bank')
        return self.env['account.journal'].search([
            *self.env['account.journal']._check_company_domain(self.env.company),
            ('type', '=', 'sale'),
        ], limit=1)

    def action_set_state_sold(self):
        idk_what_is_even_this_value_but_i_have_to_return_it = super().action_set_state_sold()
        for record in self:
            # journal = self.env['account.move'].with_context(default_move_type='out_invoice')._get_default_journal()
            journal = self._get_default_journal()
            record.env['account.move'].create(
                {'partner_id': record.buyer_id.id, 'move_type': 'out_invoice', 'journal_id': journal.id,
                 'line_ids': [
                     Command.create(
                         {
                             'name': f'Down payment for {record.name}', 'quantity': 1, 'price_unit': record.selling_price * 0.06
                         }),
                         Command.create({
                             'name': "Administrative fees", 'quantity': 1, 'price_unit': 100.00
                         })

                 ]
                 })
        return idk_what_is_even_this_value_but_i_have_to_return_it
