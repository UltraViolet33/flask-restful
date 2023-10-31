import requests

# from main import Video

BASE = "http://127.0.0.1:5000/"


# data = [{"likes": 10, "name": "Bob", "views": 1000},
#         {"likes": 15, "name": "Bobg", "views": 4000},
#         {"likes": 25, "name": "Bobh", "views": 5000}]

# for i in range(len(data)):
#     response = requests.put(BASE + "video/" + str(i), data[i])
#     print(response.json())


# response = requests.delete(BASE + "video/0")
# print(response)

# response = requests.patch(BASE + "video/2", {"name": "bob"})
# print(response.json())

new_todos = ["test1", "test2", "test3"]

def test_get_all_todos():
    response = requests.get(BASE + "todos")
    print(response.json())



def test_create_todo(todos):
    for todo in todos:
        response = requests.post(BASE + "todos", {"task":todo})
        print(response.json())



# test_get_all_todos()

test_create_todo(new_todos)