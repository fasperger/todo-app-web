import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    new_todo = st.session_state["new_todo"] + "\n"
    todos.append(new_todo)
    functions.write_todos(todos)


st.title("My ToDo App")
st.subheader("This is my ToDo App")
st.write("Increase your productivity")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="enter todos",
              label_visibility="hidden",
              placeholder="Enter a new ToDo",
              on_change=add_todo,
              key="new_todo")

st.session_state
