import psycopg2

def get_connection():
    conn = psycopg2.connect(
        host="localhost",
        database="earthquakes_db",
        user="postgres",
        password="postgres",
        port="5432"
    )
    return conn