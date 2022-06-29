{{ config(materialized='table', unique_key='company_id') }}

with

portfolio_companies as (
    select
        id,
        title,
        country,
        entry_date,
        sector
    from {{ ref('stg_web_current_portfolio') }}
),

companies_catalog as (
    select
        city,
        homepage_url,
        short_description,
        description,
        founded_on,
        employee_count,
        funding_total_usd,
        company_name,
        uuid
    from {{ ref('stg_companies') }}
),

funding_rounds as (
    select
        company_uuid,
        raised_amount_usd,
        investment_type,
        announced_on
    from {{ ref('stg_funding') }}
),

funding_rounds_agg as (
     select
        company_uuid,
        sum(raised_amount_usd) as total_raised
    from funding_rounds
    group by company_uuid
),

latest_funding_rounds as (
    select
        company_uuid,
        investment_type,
        announced_on
    from funding_rounds
    qualify row_number() over(partition by company_uuid order by announced_on desc) = 1
),

tot as (
    select
        portfolio_companies.id as company_id,
        portfolio_companies.title as company_name,
        companies_catalog.city,
        portfolio_companies.country,
        portfolio_companies.entry_date,
        portfolio_companies.sector,
        companies_catalog.homepage_url,
        companies_catalog.short_description,
        companies_catalog.description,
        companies_catalog.founded_on,
        companies_catalog.employee_count,
        funding_rounds_agg.total_raised,
        latest_funding_rounds.announced_on as last_funding_announced_on,
        latest_funding_rounds.investment_type as last_funding_investment_type
    from portfolio_companies
    left join companies_catalog
        on lower(portfolio_companies.title) = lower(companies_catalog.company_name)
    left join funding_rounds_agg
        on companies_catalog.uuid = funding_rounds_agg.company_uuid
    left join latest_funding_rounds
        on companies_catalog.uuid = latest_funding_rounds.company_uuid
)

select * from tot
