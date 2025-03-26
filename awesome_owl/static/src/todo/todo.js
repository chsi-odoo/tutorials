import {Component, useState} from '@odoo/owl'

export class TodoItem extends Component {
    static template = "awesome_owl.todo_item";

    static props = {
        id: {type: Number},
        description: {type: String},
        isCompleted: {type: Boolean},
    }
}

export class TodoList extends Component {
    static template = "awesome_owl.todo_list";

    static components = {TodoItem}

    setup() {
        this.todos = useState([
            {id: 2, description: "sell cow👹", isCompleted: false},
            {id: 3, description: "buy milk👹", isCompleted: false}
        ])
    }
}