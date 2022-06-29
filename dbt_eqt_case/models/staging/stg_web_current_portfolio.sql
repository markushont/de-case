{{ config(materialized='table', unique_key='id') }}
with

current_portfolio as (
    select
        _id as id,
        country,
        entryDate as entry_date,
        fund,
        path,
        promotedSdg as promoted_sdg,
        sdg,
        sector,
        title,
        topic,
        _fetched_time as fetched_time
    from {{ source('src_bq_raw', 'web_current_portfolio') }}
    qualify row_number() over(partition by id order by fetched_time desc) = 1
)

select * from current_portfolio
