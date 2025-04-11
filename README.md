# Finance Data Modeling & Reporting Simulation

## Overview
This project simulates an end-to-end financial reporting pipeline that modernizes data from synthetic financial transactions. The pipeline includes:
- **Data Generation:** Creating synthetic transaction data with Python.
- **Data Loading:** Using Docker to run a PostgreSQL database and loading data via dbt seeds.
- **Data Transformation:** Using dbt to build transformation models (fact & dimension tables) with built-in testing.
- **Data Visualization:** Creating interactive dashboards with Streamlit (and/or Jupyter Notebook).

## Objectives
- **Simulate a Financial Reporting Transition:**
  Mimic the modernization of legacy financial systems.
- **Develop Data Engineering Skills:**
  Work with SQL, PostgreSQL, Docker, and dbt for robust data transformations.
- **Create Interactive Visualizations:**
  Use visualization tools (Plotly & Streamlit) to analyze financial KPIs.
- **Ensure Reproducibility & Documentation:**
  Apply testing, version control, and clear documentation.

## Technologies
- **Python, Pandas, SQLAlchemy**
- **PostgreSQL (Docker)**
- **dbt (Data Build Tool)**
- **Streamlit & Plotly**
- **Git & GitHub**

## File Structure
- `finance_project/`
  - `README.md` — Project documentation
  - `requirements.txt` — Python dependencies
  - `generate_data.py` — Script to generate synthetic financial data
  - `fact_financial_transactions.csv` — CSV file generated from synthetic data
  - `dbt_project.yml` — dbt project configuration
  - `seeds/`
    - `fact_financial_transactions.csv` — CSV file for seeding data into PostgreSQL
  - `models/`
    - `src/`
      - `sources.yml` — External source definitions (raw data)
    - `example/`
      - `stg_fact_financial_transactions.sql` — Transformation model for raw data
      - `dim_date.sql` — Date dimension model
      - `my_first_dbt_model.sql` — Example model (demo)
      - `my_second_dbt_model.sql` — Example model (demo)
      - `schema.yml` — Tests for models
  - `macros/` — (Optional) Custom macros for dbt models
  - `analyses/` — (Optional) Exploratory analysis files
  - `snapshots/` — (Optional) Snapshot configurations


## How to Run the Project
1. **Set Up the Environment:**
   - Create and activate a virtual environment.
   - Install dependencies with `pip install -r requirements.txt`
2. **Database Setup:**
   - Run PostgreSQL in Docker.
   - Create the database `finance_db` and load raw data using `dbt seed`.
3. **Data Transformation:**
   - Execute `dbt run` to build transformation models.
   - Validate models with `dbt test`.
4. **Visualization:**
   - Launch the Streamlit dashboard using `streamlit run app.py`.

## What I Learned
- I learned how to generate synthetic financial data and manage it using Docker and PostgreSQL.
- I built robust transformation pipelines using dbt, including writing tests to ensure data quality.
- I developed interactive dashboards with Streamlit to deliver actionable business insights.
- I gained experience in version control and documentation, making the project reproducible and portfolio-ready.

## Future Enhancements
- Extend the dashboard with more interactivity (e.g., filtering by date or department).
- Integrate real-world financial data.
- Build additional models/dimensions to enhance reporting.


