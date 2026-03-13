import json
from pathlib import Path
from datetime import datetime
from src.db import get_connection

RAW_FOLDER = Path("data/raw")

def load_files():

    conn = get_connection()
    cur = conn.cursor()

    for file in RAW_FOLDER.glob("*.json"):

        with open(file) as f:
            data = json.load(f)

        for record in data["features"]:

            cur.execute(
                """
                INSERT INTO raw_earthquakes(fetched_at, raw_data, source_file)
                VALUES (%s, %s, %s)
                """,
                (datetime.now(), json.dumps(record), file.name)
            )

    conn.commit()
    cur.close()
    conn.close()

    print("Loaded earthquake data into database")

if __name__ == "__main__":
    load_files()