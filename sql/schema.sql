CREATE TABLE dim_location (
  location_code VARCHAR(10) PRIMARY KEY
);

CREATE TABLE dim_store (
  store_id INTEGER PRIMARY KEY,
  store_type CHAR(1) NOT NULL,
  size_raw DECIMAL(12,2),
  location_code VARCHAR(10) NOT NULL REFERENCES dim_location(location_code)
);

CREATE TABLE dim_department (
  department_id INTEGER PRIMARY KEY
);

CREATE TABLE dim_date (
  date_key DATE PRIMARY KEY,
  year_num SMALLINT NOT NULL,
  month_num SMALLINT NOT NULL,
  quarter_num SMALLINT NOT NULL,
  iso_week SMALLINT NOT NULL,
  is_holiday BOOLEAN NOT NULL
);

-- Grain: one row per store, department, week.
CREATE TABLE fact_weekly_sales (
  store_id INTEGER NOT NULL REFERENCES dim_store(store_id),
  department_id INTEGER NOT NULL REFERENCES dim_department(department_id),
  date_key DATE NOT NULL REFERENCES dim_date(date_key),
  weekly_sales DECIMAL(16,2) NOT NULL,
  PRIMARY KEY (store_id, department_id, date_key)
);

-- Grain: one row per store and week. Kept separate from sales to avoid
-- repeating contextual values for every department.
CREATE TABLE fact_store_features (
  store_id INTEGER NOT NULL REFERENCES dim_store(store_id),
  date_key DATE NOT NULL REFERENCES dim_date(date_key),
  temperature DECIMAL(12,4),
  fuel_price DECIMAL(12,4),
  markdown1 DECIMAL(16,2), markdown2 DECIMAL(16,2),
  markdown3 DECIMAL(16,2), markdown4 DECIMAL(16,2), markdown5 DECIMAL(16,2),
  cpi DECIMAL(16,8), unemployment DECIMAL(12,4),
  fuel_price_scale_suspect BOOLEAN NOT NULL,
  unemployment_scale_suspect BOOLEAN NOT NULL,
  PRIMARY KEY (store_id, date_key)
);
