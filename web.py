import streamlit as st
import functions
todos = functions.get_todos()
st.title("My Todo App")


def add_todo():
    todo = st.session_state['new_todo'] + "\n"
    todos.append(todo)
    functions.write_todos(todos)


for index, item in enumerate(todos):
    checkbox = st.checkbox(item, key=item)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[item]
        st.experimental_rerun()


st.text_input(label="Enter a todo", label_visibility='hidden',
              placeholder="Add a new todo...", on_change=add_todo, key='new_todo')
st.session_state
