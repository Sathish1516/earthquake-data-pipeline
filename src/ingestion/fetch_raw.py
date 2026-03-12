import requests
import json
from datetime import datetime,timezone
from pathlib import Path

URL = "https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&limit=20"

def fetch_earthquakes():

    response = requests.get(URL)
    data = response.json()

    timestamp = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")

    filename = f"earthquakes_{timestamp}.json"
    filepath = Path("data/raw") / filename

    with open(filepath, "w") as f:
        json.dump(data, f)

    print(f"Saved raw data to {filepath}")

if __name__ == "__main__":
    fetch_earthquakes()