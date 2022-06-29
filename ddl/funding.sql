create or replace table `eqt-case-354813.eqt_case_raw.funding`
(
    funding_round_uuid string not null,
    company_uuid string not null,
    company_name string,
    investment_type string,
    announced_on date,
    raised_amount_usd float,
    investor_count integer
)
