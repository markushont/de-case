import json
from lib.logging import LoggerFactory
from lib.models.AppConfig import AppConfig

from lib.models.EqtWebTableScraperConfig import EqtWebTableScraperConfig
from scrape_eqt_page import scrape_eqt_page

logger = LoggerFactory.create_logger()


def scrape_pages(app_config, page_configs):
    for config in page_configs:
        logger.info(f"Handling table {config.table_name}")
        # TODO: handle exceptions and fail after all pages had time to finish
        scrape_eqt_page(app_config=app_config, page_config=config)

if __name__ == '__main__':
    app_config = AppConfig.from_environment()

    with open('page_configs.json', 'r') as f:
        page_configs_dict = json.load(f)
        page_configs = [
            EqtWebTableScraperConfig.from_dict(config)
            for config in page_configs_dict
        ]

    scrape_pages(app_config=app_config, page_configs=page_configs)
