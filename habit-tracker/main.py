import requests
from datetime import datetime

USERNAME = "username"
TOKEN = "your token"
GRAPHID = "your graph id"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",

}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPHID,
    "name": "CODETRACKER",
    "unit": "hours",
    "type": "float",
    "color": "momiji",
    "timezone": "Asia/Kolkata"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

posting_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}"

today = datetime.now()

pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How much time you have code today? ")
}

# response = requests.post(url=posting_pixel_endpoint, json=pixel_config, headers=headers)
# print(response.text)

updating_pixel = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}/{today.strftime('%Y%m%d')}"

new_pixel_data = {
    "quantity": "4.5",
}

updating_pixel = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}/{today.strftime('%Y%m%d')}"

new_pixel_data = {
    "quantity": "4.5",
}

# response = requests.put(url=updating_pixel, json=new_pixel_data, headers=headers)
# print(response.text)


deleting_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}/20230605"

# response = requests.delete(url=deleting_pixel_endpoint, headers=headers)
# print(response.text)
