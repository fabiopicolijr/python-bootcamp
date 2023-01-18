import requests
from datetime import datetime

USERNAME = "fabiopicolijr"
TOKEN = "6PSao1799!"
GRAPH_ID = "graph1"
DATE = datetime.now().strftime("%Y%m%d")

pixela_endpoint = "https://pixe.la/v1/users"

pixel_update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{DATE}"

headers = {
    "X-USER-TOKEN": TOKEN
}

# print(new_pixel_data)

response = requests.delete(url=pixel_update_endpoint, headers=headers)
print(response.text)