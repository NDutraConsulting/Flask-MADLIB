DROP TABLE if exists business_madlib;
CREATE TABLE business_madlib (
    id INTEGER PRIMARY KEY autoincrement,
    business_name TEXT NOT NULL,
    business_type TEXT NOT NULL,
    market_type TEXT NOT NULL,
    job_to_be_done TEXT NOT NULL,
    revenue_model TEXT NOT NULL
);
