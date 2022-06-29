{{ config(materialized='table', unique_key='uuid') }}
with

companies as (
    select
        uuid,
        company_name,
        homepage_url,
        country_code,
        city,
        short_description,
        description,
        founded_on,
        last_funding_on,
        funding_rounds,
        funding_total_usd,
        employee_count
    from {{ source('src_bq_raw', 'companies') }}
)

select * from companies
