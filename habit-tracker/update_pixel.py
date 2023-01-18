import requests
from datetime import datetime

USERNAME = "fabiopicolijr"
TOKEN = "6PSao1799!"
GRAPH_ID = "graph1"
DATE = datetime.now().strftime("%Y%m%d")

pixela_endpoint = "https://pixe.la/v1/users"

pixel_update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{DATE}"

print(pixel_update_endpoint)

new_pixel_data = {
    "quantity": "15"
}
headers = {
    "X-USER-TOKEN": TOKEN
}

# print(new_pixel_data)

response = requests.put(url=pixel_update_endpoint, json=new_pixel_data, headers=headers)
print(response.text)