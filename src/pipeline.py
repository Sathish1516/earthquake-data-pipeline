from src.ingestion.fetch_raw import fetch_earthquakes
from src.ingestion.load_to_db import load_files
from src.transform.clean_earthquakes import transform
from src.analytics.build_daily_summary import build_summary

def run_pipeline():

    print("Starting Pipeline...")

    fetch_earthquakes()
    load_files()
    transform()
    build_summary()

    print("Pipeline completed successfully")

if __name__ == "__main__":
    run_pipeline()  