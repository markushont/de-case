create or replace external table `eqt-case-354813.eqt_case_raw.web_divestments` (
    _id string not null,
    country string,
    entryDate date,
    exitDate date,
    fund string,
    path string,
    sector string,
    title string
) options (
    format = 'JSON',
    uris = ['gs://markus-hont-eqt-scraper/divestments/*.json']
)
