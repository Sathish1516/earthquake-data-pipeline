# 🌍 Earthquake Data Pipeline

An end-to-end data engineering pipeline that ingests real-time earthquake data from the USGS API, processes and validates it, and generates analytical insights.

---

## 🚀 Features

* API-based ingestion (USGS Earthquake API)
* Raw data storage using JSONB
* Data validation with rejected records tracking
* Incremental processing using checkpointing
* Analytics layer (daily summaries)
* Batch processing optimization
* Logging for monitoring & debugging
* Fully Dockerized (one-command execution)

---

## 🏗️ Architecture

```
API → Raw Layer → Validation → Staging → Analytics → Logs
```

---

## 📂 Project Structure

```
src/
 ├── ingestion/
 ├── transform/
 ├── analytics/
 ├── db.py
 ├── logger.py
 └── pipeline.py
```

---

## ⚙️ Tech Stack

* Python
* PostgreSQL
* Docker
* psycopg2
* Requests

---

## ▶️ Run the Pipeline

### Local Run

```
python -m src.pipeline
```

### Docker Run (Recommended)

```
docker compose up --build
```

---

## 📊 Example Output

| date       | total_events | avg_magnitude | avg_depth |
| ---------- | ------------ | ------------- | --------- |
| 2026-03-30 | 20           | 1.67          | 10.2      |

---

## 🧠 Key Concepts Implemented

* ETL Pipeline Design
* Incremental Data Processing
* Data Validation & Error Handling
* Batch Inserts & Indexing
* Logging & Monitoring
* Containerized Deployment

---

## 📌 Future Improvements

* Airflow orchestration
* Kafka streaming ingestion
* Data warehouse integration (BigQuery/Snowflake)

---
