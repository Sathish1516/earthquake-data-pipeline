CREATE TABLE raw_earthquakes (
    id SERIAL PRIMARY KEY,
    fetched_at TIMESTAMP,
    raw_data JSONB,
    source_file TEXT
);

CREATE TABLE staging_earthquakes (
    id SERIAL PRIMARY KEY,
    event_id TEXT UNIQUE,
    magnitude FLOAT,
    place TEXT,
    event_time TIMESTAMP,
    longitude FLOAT,
    latitude FLOAT,
    depth FLOAT,
    raw_id INTEGER
);

CREATE TABLE rejected_earthquakes (
    id SERIAL PRIMARY KEY,
    raw_id INTEGER,
    reason TEXT,
    raw_data JSONB,
    rejected_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE pipeline_state (
    id SERIAL PRIMARY KEY,
    last_raw_id INTEGER
);

INSERT INTO pipeline_state (last_raw_id) VALUES (0);

CREATE TABLE daily_earthquake_summary (
    date DATE PRIMARY KEY,
    total_events INTEGER,
    avg_magnitude FLOAT,
    avg_depth FLOAT
);