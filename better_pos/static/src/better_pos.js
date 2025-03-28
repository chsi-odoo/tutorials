/** @odoo-module **/

import { patch } from "@web/core/utils/patch";
import { PosStore } from "@point_of_sale/app/store/pos_store";
import { ProductScreen } from "@point_of_sale/app/screens/product_screen/product_screen";
import {
    BACKSPACE
} from "@point_of_sale/app/generic_components/numpad/numpad";
import { ControlButtons } from "@point_of_sale/app/screens/product_screen/control_buttons/control_buttons";
import { useService } from "@web/core/utils/hooks";

patch(PosStore.prototype, {
    async getProductInfo(product, quantity, priceExtra = 0) {
        const baseProductInfo = await super.getProductInfo(...arguments);
        const productInfo = baseProductInfo.productInfo;

        // console.log(this.models["product.product"])
        const actualProduct = this.data.models["product.product"].get(product.id);
        // const actualProduct2 = this.models["product.product"].get(product.id);
        // console.log(actualProduct);
        // console.log(actualProduct2)
        productInfo.weight = actualProduct.weight
        productInfo.volume = actualProduct.volume
        // return baseProductInfo
        return baseProductInfo
    }
})
//
// patch(ProductScreen.prototype, {
//     onClickRemoveButton() {
//         console.log(this.numberBuffer)
//         const backspaceValue = BACKSPACE.value
//         this.numberBuffer.sendKey(backspaceValue);
//         this.numberBuffer.sendKey(backspaceValue);
//     }
// })

patch(ControlButtons.prototype, {
    setup() {
      super.setup()
        this.numberBuffer = useService("number_buffer");
        
    },
    onClickRemoveButton() {
        console.log(this.numberBuffer)
        const backspaceValue = BACKSPACE.value
        // this.pos.numpadMode = 'quantity'
        // this.numberBuffer.state.buffer = null;
                // the buffer should not be in reset state anymore.
        // this.numberBuffer.isReset = false;
        // it should not be in a start the buffer over state anymore.
        // this.numberBuffer.state.toStartOver = false;
        // this.numberBuffer.reset();
        // this.numberBuffer.trigger("buffer-update", this.numberBuffer.state.buffer);
        // this.numberBuffer.reset();

        this.pos.numpadMode = 'quantity'
        const numberBuffer = this.numberBuffer;
        numberBuffer.isReset = false;
        numberBuffer.state.buffer = null;
        this.numberBuffer.sendKey(backspaceValue);
        // this.numberBuffer.trigger("buffer-update", this.numberBuffer.state.buffer);
    }
})

patch(PosStore.prototype, {
        getReceiptHeaderData(order) {
            const baseData = super.getReceiptHeaderData(...arguments);

        return {
            ...baseData,
            congratulatory_text: this.config.congratulatory_text
        };
    }
})
// patch(, {
//     get_product_info_pos(self, price, quantity, pos_config_id) {
//
//     }
// })