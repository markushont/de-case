create or replace table `eqt-case-354813.eqt_case_raw.companies`
(
    uuid string not null,
    company_name string,
    homepage_url string,
    country_code string,
    city string,
    short_description string,
    description string,
    founded_on date,
    last_funding_on date,
    funding_rounds integer,
    funding_total_usd float,
    employee_count string,
)