import requests

BASE = "http://127.0.0.1:5000/"

new_todos = ["test1", "test2", "test3"]

def test_get_all_todos():
    response = requests.get(BASE + "todos")
    print(response.json())

def test_create_todo(todos):
    for todo in todos:
        response = requests.post(BASE + "todos", {"task":todo})
        print(response.json())



test_get_all_todos()

test_create_todo(new_todos)