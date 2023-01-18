import requests
from datetime import datetime

USERNAME = "fabiopicolijr"
TOKEN = "6PSao1799!"
GRAPH = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"


pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH}"


yesterday = datetime(year=2030, month=1, day=16) # only to show functionality
today = datetime.now()

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "9.7"
}
headers = {
    "X-USER-TOKEN": TOKEN
}

print(pixel_data)

response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print(response.text)