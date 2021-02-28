import requests
from datetime import datetime

KEY = ""
ID = ""

GENDER = "male"
WEIGHT_KG = "70"
HEIGHT_CM = "172"
AGE = "30"

exercise_endpoint = ""
sheet_endpoint = ""

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": ID,
    "x-app-key": KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
exercises = result["exercises"][0]

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

sheet_inputs = {
    "workout": {
        "date": today_date,
        "time": now_time,
        "exercise": exercises["user_input"].title(),
        "duration": exercises["duration_min"],
        "calories": exercises["nf_calories"]
    }
}

bearer_headers = {
    "Authorization": ""
}
sheet_response = requests.post(
    sheet_endpoint,
    json=sheet_inputs,
    headers=bearer_headers
)

print(sheet_response.text)
