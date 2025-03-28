/** @odoo-module **/

import { patch } from "@web/core/utils/patch";
import { PosStore } from "@point_of_sale/app/store/pos_store";

patch(PosStore.prototype, {
    async getProductInfo(product, quantity, priceExtra = 0) {
        const baseProductInfo = await super.getProductInfo(...arguments);
        const productInfo = baseProductInfo.productInfo;

        console.log(this.models["product.product"])
        const actualProduct = this.data.models["product.product"].get(product.id);
        const actualProduct2 = this.models["product.product"].get(product.id);
        console.log(actualProduct);
        console.log(actualProduct2)
        productInfo.weight = actualProduct.weight
        productInfo.volume = actualProduct.volume
        // return baseProductInfo
        return baseProductInfo
    }
})

// patch(, {
//     get_product_info_pos(self, price, quantity, pos_config_id) {
//
//     }
// })