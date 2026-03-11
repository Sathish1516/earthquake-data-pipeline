import requests
from datetime import datetime

URL = "https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&limit=5"

response = requests.get(URL)
data = response.json()

print("Keys in response:")
print(data.keys())

print("\nNumber of events:")
print(len(data["features"]))

first_event = data["features"][0]

print("\nKeys inside one event:")
print(first_event.keys())

print("\nProperties fields:")
print(first_event["properties"].keys())

properties = first_event["properties"]

print("\nSample event data:")
print("Magnitude:", properties["mag"])
print("Place:", properties["place"])

timestamp_ms = properties["time"]
timestamp = datetime.fromtimestamp(timestamp_ms / 1000)

print("Event time:", timestamp)