import {Component, useState} from '@odoo/owl'
import {useAutofocus} from "../utils";

export class TodoItem extends Component {
    static template = "awesome_owl.todo_item";

    static props = {
        id: {type: Number},
        description: {type: String},
        isCompleted: {type: Boolean},
        onClick: {type: Function},
        onRemove: {type: Function},
    };

    setup() {

    }

    handleCheck(e) {
        console.log('handleCheck')
        console.log(this)
        console.log(e)
        this.props.onClick(this, e.target.checked)
    }

    handleRemove(e) {
        this.props.onRemove(this)
    }
}

export class TodoList extends Component {
    static template = "awesome_owl.todo_list";

    static components = {TodoItem}

    setup() {
        this.todos = useState([
            {id: 1, description: "sell cow👹", isCompleted: true},
            {id: 2, description: "buy milk👹", isCompleted: false}
        ])

        this.uniqueNextItemId = this.todos.length + 1


        useAutofocus('input-box')

        // works without binding if we do onClick="(a,b) => {this.toggleState(a,b);}"
        // this.toggleState = this.toggleState.bind(this)
    }

    addTodo(keyBoardEvent) {
        if (keyBoardEvent.code !== "Enter") {
            return;
        }
        const description = keyBoardEvent.target.value;
        if (!description) {
            return;
        }

        // const id = this.todos.length + 1;
        this.todos.push({id: this.uniqueNextItemId, description: keyBoardEvent.target.value, isCompleted: false});
        this.uniqueNextItemId = this.uniqueNextItemId+1
    }

    toggleState(item, isChecked) {
        console.log('toggleState')
        console.log(this)
        console.log(item)
        console.log(isChecked)
        const correspondingTodoItem = this.todos.find((todoItem) => todoItem.id === item.props.id)
        correspondingTodoItem.isCompleted = isChecked;
        console.log(isChecked)

        console.log(correspondingTodoItem)
    }

    removeItem(item) {
        const index = this.todos.findIndex((x) => x.id === item.props.id);
        if (index >= 0) {
            this.todos.splice(index,1)
        }
    }
}