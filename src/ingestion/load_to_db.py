import json
from pathlib import Path
from datetime import datetime
from src.db import get_connection
from psycopg2.extras import execute_batch

RAW_FOLDER = Path("data/raw")

def load_files():

    conn = get_connection()
    cur = conn.cursor()

    for file in RAW_FOLDER.glob("*.json"):

        with open(file) as f:
            data = json.load(f)

        records = []
        for record in data["features"]:
            records.append((
                datetime.now(),
                json.dumps(record),
                file.name
            ))
        execute_batch(cur, """
            INSERT INTO raw_earthquakes (fetched_at, raw_data, source_file) VALUES (%s, %s, %s)""", 
            records)
        
    conn.commit()
    cur.close()
    conn.close()

    print("Loaded earthquake data into database")

if __name__ == "__main__":
    load_files()