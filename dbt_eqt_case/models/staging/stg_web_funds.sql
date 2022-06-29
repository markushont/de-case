{{ config(materialized='table', unique_key='title') }}
with

funds as (
    select
        currency,
        launchDate as launch_date,
        path,
        size,
        status,
        title,
        _fetched_time as fetched_time
    from {{ source('src_bq_raw', 'web_funds') }}
    qualify row_number() over(partition by title order by fetched_time desc) = 1
)

select * from funds
