import json
import os

from lib.models.EqtWebTableScraperConfig import EqtWebTableScraperConfig

def scrape_page(app_config, page_config):
    pass

def scrape_pages(app_config, page_configs):
    for config in page_configs:
        # TODO: handle exceptions and fail after all pages finished
        scrape_page(app_config=app_config, page_config=config)

if __name__ == '__main__':
    app_config = {
        'gc_private_key_id': os.environ['GC_PRIVATE_KEY_ID'],
        'gc_private_key': os.environ['GC_PRIVATE_KEY'],
        'gc_client_email': os.environ['GC_CLIENT_EMAIL'],
        'gc_client_id': os.environ['GC_CLIENT_ID'],
        'gc_token_uri': os.environ['GC_TOKEN_URI'],
        'gc_project_id': os.environ['GC_PROJECT_ID'],
        'target_bucket': os.getenv('TARGET_BUCKET', 'markus-hont-eqt-scraper')
    }

    with open('page_configs.json', 'r') as f:
        page_configs_dict = json.load(f)
        page_configs = [
            EqtWebTableScraperConfig.from_dict(name, config)
            for name, config in page_configs_dict.items()
        ]

    scrape_pages(app_config=app_config, page_configs=page_configs)
