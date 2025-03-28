from odoo import api, models

class ProductProduct(models.Model):
    _name = 'product.product'
    _inherit = ['product.product', 'pos.load.mixin']

    @api.model
    def _load_pos_data_fields(self, config_id):
        return [
            'id', 'display_name', 'lst_price', 'standard_price', 'categ_id', 'pos_categ_ids', 'taxes_id', 'barcode', 'name',
            'default_code', 'to_weight', 'uom_id', 'description_sale', 'description', 'product_tmpl_id', 'tracking', 'type', 'service_tracking', 'is_storable',
            'write_date', 'available_in_pos', 'attribute_line_ids', 'active', 'image_128', 'combo_ids', 'product_template_variant_value_ids', 'product_tag_ids',
            'weight', 'volume'
        ]
