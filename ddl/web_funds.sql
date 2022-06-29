create or replace external table `eqt-case-354813.eqt_case_raw.web_raw` (
    currency string,
    launchDate string,
    path string,
    size string,
    status string,
    title string,
    _fetched_time timestamp
)
options (
    format = 'JSON',
    uris = ['gs://markus-hont-eqt-scraper/funds/*.json']
)