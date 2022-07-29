import requests

from main import Video

BASE = "http://127.0.0.1:5000/"


# data = [{"likes": 10, "name": "Bob", "views": 1000},
#         {"likes": 15, "name": "Bobg", "views": 4000},
#         {"likes": 25, "name": "Bobh", "views": 5000}]

# for i in range(len(data)):
#     response = requests.put(BASE + "video/" + str(i), data[i])
#     print(response.json())


# response = requests.delete(BASE + "video/0")
# print(response)

response = requests.patch(BASE + "video/2", {"name": "bob"})
print(response.json())
