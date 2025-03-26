/** @odoo-module **/

import {Component, useState, markup} from "@odoo/owl";
import {Counter} from "./counter/counter";
import {Card} from "./card/card";
import {TodoList} from "./todo/todo";

export class Playground extends Component {
    static template = "awesome_owl.playground";

    static components = {Counter, Card, TodoList};

    setup() {
        this.incrementSum = this.incrementSum.bind(this)

        // cant seem to find a better way to get it to work without using useState
        this.counterInitialValues = Playground.counterInitialValues
    }

    static defaultProps = {
        counterInitialValues: [2,5],
    }

    static counterInitialValues = [2, 5]

    state = useState({value: Playground.counterInitialValues.reduce((a, b) => a + b)})

    //called in xml
    //i wonder why this can be called directly
    dangerousUnescapedValue = markup`<div class=\'text-primary\'>i am blue</div>`

    increment() {
        this.state.value++;
    }

    //callback passed to children
    incrementSum() {
        this.increment()
    }
}
