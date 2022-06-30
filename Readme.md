# EQT Data Engineering Case 2022-06-29

# Project Structure

* `ddl`: Create tables for staging raw data
* `scraper`: Python source code for ingesting data with a scraper
* `dbt_eqt_case`: Data modeling project

# Testing
* To test the scraper, navigate to `scraper/` and run `PYTHONPATH="$PYTHONPATH:./src" pytest`
