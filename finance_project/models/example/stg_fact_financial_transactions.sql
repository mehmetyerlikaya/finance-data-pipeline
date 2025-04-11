{{ config(materialized='table') }}

SELECT
    transaction_id,
    transaction_date,
    amount,
    cost,
    department_id,
    product_id
FROM {{ source('raw_financial', 'fact_financial_transactions') }}
