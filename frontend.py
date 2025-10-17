import streamlit as st
import requests

API_URL = 'http://127.0.0.1:8000/todos'

st.title('To-Do App')

def fetch_todos():
    response = requests.get(API_URL)
    return response.json()

def add_todo(task):
    todo = {'id': len(fetch_todos()) + 1, 'task': task, 'completed': False}
    requests.post(API_URL, json=todo)

todos = fetch_todos()

for todo in todos:
    st.checkbox(todo['task'], value=todo['completed'])

new_task = st.text_input('Add a new task')
if st.button('Add'): 
    add_todo(new_task)
    st.experimental_rerun()
