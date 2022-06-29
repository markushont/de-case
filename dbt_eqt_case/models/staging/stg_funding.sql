{{ config(materialized='table', unique_key='funding_round_uuid') }}
with

funding_rounds as (
    select
        funding_round_uuid,
        company_uuid,
        company_name,
        investment_type,
        announced_on,
        raised_amount_usd,
        investor_count,
        investor_names
    from {{ source('src_bq_raw', 'funding') }}
)

select * from funding_rounds
