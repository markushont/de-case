create or replace external table `eqt-case-354813.eqt_case_raw.web_current_portfolio` (
    _id string not null,
    country string,
    entryDate date,
    fund json,
    path string,
    promotedSdg string,
    sdg json,
    sector string,
    title string,
    topic string,
    _fetched_time timestamp
)
options (
    format = 'JSON',
    uris = ['gs://markus-hont-eqt-scraper/current_portfolio/*.json']
)