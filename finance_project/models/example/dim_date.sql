{{ config(materialized='table') }}

with distinct_dates as (
    select distinct transaction_date
    from {{ ref('stg_fact_financial_transactions') }}
)

select
    row_number() over (order by transaction_date) as date_id,
    transaction_date,
    extract(day from transaction_date) as day,
    extract(month from transaction_date) as month,
    extract(year from transaction_date) as year
from distinct_dates