import {useRef, onMounted} from "@odoo/owl"

export const useAutofocus = (refTag) => {
    const ref = useRef(refTag)
    onMounted(() => ref.el.focus())
}