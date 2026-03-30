from src.db import get_connection
from src.logger import get_logger
logger = get_logger()

def build_summary():

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("DELETE FROM daily_earthquake_summary")

    cur.execute("""
                INSERT INTO daily_earthquake_summary (date , total_events , avg_magnitude , avg_depth)
                SELECT DATE(event_time) AS date,
                COUNT(*) AS total_events,
                AVG(magnitude) AS avg_magnitude,
                AVG(depth) AS avg_depth
                FROM staging_earthquakes
                GROUP BY DATE(event_time)
                """)
    
    conn.commit()
    cur.close()
    conn.close()    
    logger.info("Building daily summary")
    logger.info("Summary build complete")

if __name__ == "__main__":
    build_summary()