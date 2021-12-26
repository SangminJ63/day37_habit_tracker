import requests
from datetime import datetime

USER_NAME = "sangminjeon"
TOKEN = "thisissecret1212"
GRAPH_ID = "graph1"
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {"token": TOKEN,
               "username": "sangminjeon",
               "agreeTermsOfService": "yes",
               "notMinor": "yes"}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)

graph_pixel_endpoint = f"{graph_endpoint}/{GRAPH_ID}"

today = datetime.now()
print(today.strftime("%Y%m%d"))

graph_pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "15.12"
}

# response = requests.post(url=graph_pixel_endpoint, json=graph_pixel_data, headers=headers)
# print(response.text)

pixel_update_endpoint = f"{graph_pixel_endpoint}/20211225"

# response = requests.put(url=pixel_update_endpoint, json={"quantity": "12.74"}, headers=headers)
# print(response)

delete_endpoint = f"{graph_pixel_endpoint}/20211225"

# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)