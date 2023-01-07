import streamlit as st
import todoFunctions

todos = todoFunctions.get_todos()
def add_todo():
    todo =st.session_state['new_todo'] + "\n"
    todos.append(todo)
    todoFunctions.write_todos(todos)

st.title("Rancy's ToDo App")
st.subheader("This is my ToDo App")
st.write("To increase my productivity")

todos = todoFunctions.get_todos()

for index,todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        todoFunctions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="input", placeholder="Add new ToDo...",
              on_change=add_todo, key="new_todo", label_visibility="hidden")
