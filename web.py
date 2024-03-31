import streamlit as st
import functions


todos = functions.get_todos()


def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)


st.title("Todo app")
st.subheader("List your todo below")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo] # deleted from session stat dictionary
        st.rerun()

st.text_input(label="Add a new todo...", label_visibility= "hidden", placeholder="Add a new todo...",
              on_change=add_todo, key="new_todo")