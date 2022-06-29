import json
from lib.models.AppConfig import AppConfig

from lib.models.EqtWebTableScraperConfig import EqtWebTableScraperConfig
from scrape_eqt_page import scrape_eqt_page

def scrape_pages(app_config, page_configs):
    for config in page_configs:
        # TODO: handle exceptions and fail after all pages had time to finish
        scrape_eqt_page(app_config=app_config, page_config=config)

if __name__ == '__main__':
    app_config = AppConfig.from_environment()

    with open('page_configs.json', 'r') as f:
        page_configs_dict = json.load(f)
        page_configs = [
            EqtWebTableScraperConfig.from_dict(name, config)
            for name, config in page_configs_dict.items()
        ]

    scrape_pages(app_config=app_config, page_configs=page_configs)
