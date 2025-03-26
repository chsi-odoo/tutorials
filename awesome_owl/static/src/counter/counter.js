import {Component, xml, useState} from "@odoo/owl"

export class Counter extends Component {
    static template = "awesome_owl.counter"

    static props = {
        initialValue: Number,
        onChange: {type: Function, optional: true}
    };

    state = useState({value: this.props.initialValue});

    increment() {
        this.state.value++;
        this.props.onChange()
    }
}