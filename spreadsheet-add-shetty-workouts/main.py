import requests
from datetime import datetime
from os import environ

APP_ID = "5d5dc127"
API_KEY = "4caf7fd57c957d09ebd0c2b154aec3b1"
now_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

age = 38
gender = "male"
weight_kg = "71"
height_cm = "176"

nutritionix_version = "v2"
nutritionix_endpoint = f"https://trackapi.nutritionix.com/{nutritionix_version}"
exercise_endpoint = f"{nutritionix_endpoint}/natural/exercise"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json"
}

query_text = input("Tell me which exercise you did: ")

exercise_data = {
    "query": query_text,
    "gender": gender,
    "weight_kg": weight_kg,
    "height_cm": height_cm,
    "age": age
}

response = requests.post(url=exercise_endpoint, json=exercise_data, headers=headers)
exercises = response.json()["exercises"]

sheety_add_endpoint = "https://api.sheety.co/c3871954a0a3d4a8077e875026d8e2c8/workoutTracking/workouts"

bearer_headers = {
    "Authorization": f"Bearer {environ['COMPUTERNAME']}"  # I do this because I cant create env variables on this PC.
}

print(bearer_headers)

for exercise in exercises:
    sheety_data = {
        "workout": {
            "date": now_date,
            "time": now_time,
            "exercise": exercise["user_input"],
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],

        }
    }
    sheet_response = requests.post(url=sheety_add_endpoint, json=sheety_data, headers=bearer_headers)
    print(sheet_response.text)


