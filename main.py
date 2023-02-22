import requests
from datetime import datetime

USERNAME = "dhyan"
TOKEN = "jdisllskaojaoxox67680"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token":TOKEN,
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id":"graph1",
    "name":"Reading Graph",
    "unit":"minutes",
    "type":"int",
    "color":"sora"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1"

today = datetime.today().strftime("%Y%m%d")

pixel_data = {
    "date":today,
    "quantity":input("How many minutes did you read today?")
}

response = requests.post(url=pixel_endpoint, json=pixel_data, headers=headers)
print(response.text)

pixel_update = {
    "quantity":"10"
}

# delete_pixel = requests.delete(url=f"{pixela_endpoint}/{USERNAME}/graphs/graph1/{yesterday}", headers=headers)
# print(delete_pixel.text)