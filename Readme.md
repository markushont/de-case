# Data Engineering Case 2022-06-29

# Project Structure

* `ddl`: Create tables for staging raw data
* `scraper`: Python source code for ingesting data with a scraper
* `dbt_eqt_case`: Data modeling project

# Running
* `ddl`: Execute statements in a query console
* `scraper`: Navigate to `scraper/`, export environment variables according to `scraper/src/lib/models/AppConfig.py` and run `python main.py`
* `dbt_eqt_case`: Navigate to `dbt_eqt_case/` and run `dbt run`

# Testing
## Scraper
To test the scraper, navigate to `scraper/` and run `PYTHONPATH="$PYTHONPATH:./src" pytest`

## dbt project
To test the dbt project, navigate to `dbt_eqt_case/` and run `dbt test`. One test is failing because there are funding rounds in the source data that don't have a corresponding company

# Suggested TODOs before going live ;)

* **ddl:** Manage raw data DDLs with a schema migrations tool, e.g. Alembic
* **scraper:** Implement more unit tests for business logic
* **scraper:** Implement more component tests with mocked dependencies
* **scraper:** Errors and logging
  - Handle cases when scraped data doesn't match configured columns
  - If one individual sub-scraper fails, allow others to finish before raising exceptions or crashing
* **scraper:** Would have to think carefully about how to implement it but it could maybe be cool to be able traverse page data and follow paths like in the suggestion in `page_configs_next_level.json` where e.g. the funds page is referring to a company (which is referring to people). An alternative could be to get the page tree from the web page if it exists and maintain a flat set of data with all the routes (funds, companies, people, etc) and handle linking at a later stage after ingestion.
* **dbt_eqt_case:** More tests and documentation
* **dbt_eqt_case:** I was unable to parse json objects into something useful in BigQuery (due to my billing plan?), so it remains to link `stg_web_current_portfolio` to `stg_web_funds`. In other data platforms such as Snowflake this is a simple task.
* **general:** Schedule pipeline in e.g. Airflow. It would then be possible to parallelize the scraper jobs also so that if one page fails it won't affect the others.
* **general:** Release pipelines
