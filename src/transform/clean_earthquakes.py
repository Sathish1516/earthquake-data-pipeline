from src.db import get_connection
from datetime import datetime
import json
def convert_time(ms):
    if not ms:
        return None
    return datetime.fromtimestamp(ms / 1000)

def  is_valid(event_id, magnitude, event_time, coordinates):
    
    if not event_id:
        return False, "missing event_id"
    
    if magnitude is None:
        return False, "missing magnitude"
    
    if event_time is None:
        return False, "invalid_event_time"
    
    if not coordinates or len(coordinates) < 3:
        return False, "missing_coordinates"
    
    return True, None

def transform():

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT id, raw_data FROM raw_earthquakes") 
    rows = cur.fetchall()

    for raw_id, raw in rows:

        properties = raw.get("properties", {})
        geometry = raw.get("geometry", {})

        coordinates = geometry.get("coordinates", [None, None, None])

        event_id = raw.get("id")
        magnitude = properties.get("mag")
        place = properties.get("place")
        event_time = convert_time(properties.get("time"))

        longitude = coordinates[0]
        latitude = coordinates[1]
        depth = coordinates[2]

        valid , reason = is_valid(event_id, magnitude, event_time, coordinates)

        if not valid:
            cur.execute("""
                        INSERT INTO rejected_earthquakes(raw_id, reason, raw_data)
                        VALUES (%s, %s, %s)
                        """, (raw_id, reason, json.dumps(raw)))
            continue
        
        cur.execute(
            """
            INSERT INTO staging_earthquakes
            (event_id, magnitude , place , event_time , longitude , latitude , depth , raw_id)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
            ON CONFLICT (event_id) DO NOTHING
            """,(
                event_id, magnitude, place, event_time, 
                longitude, latitude, depth, raw_id  
            ))
        
    conn.commit()
    cur.close()
    conn.close()

    print("Staging load complete")

if __name__ == "__main__":
    transform()