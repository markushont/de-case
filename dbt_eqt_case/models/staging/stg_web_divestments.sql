{{ config(materialized='table', unique_key='id') }}
with

divestments as (
    select
        _id as id,
        country,
        entryDate as entry_date,
        exitDate as exit_date,
        fund,
        path,
        sector,
        title,
        _fetched_time as fetched_time
    from {{ source('src_bq_raw', 'web_divestments') }}
    qualify row_number() over(partition by id order by fetched_time desc) = 1
)

select * from divestments
