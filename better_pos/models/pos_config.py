from odoo import api, models, fields

class PosConfig(models.Model):
    # _name = 'pos.config'
    _inherit = 'pos.config'

    congratulatory_text = fields.Text(string="Congratulatory text", help="Text to be displayed in the PoS receipt")