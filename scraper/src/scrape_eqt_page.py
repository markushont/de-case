from typing import List

import requests

from lib.logging import LoggerFactory
from lib.models.AppConfig import AppConfig
from lib.models.EqtWebTableScraperConfig import EqtWebTableScraperConfig
from lib.models.ScrapingException import ScrapingException

logger = LoggerFactory.create_logger()

def _safe_get_object_from_path(dct, path):
    if len(path) > 1 and path[0] in dct:
        return _safe_get_object_from_path(dct[path[0]], path[1:])
    elif len(path) > 0 and path[0] in dct:
        return dct.get(path[0], None)
    else:
        return None

def _get_page_data_json(url: str):
    res = requests.get(url=url)

    if not res.ok:
        logger.warn('Could not fetch url', extra={'url': url, 'status': res.status_code, 'response': res.text})

    return res.json() if res.ok else None

def _collect_and_validate_table_rows(page_data, table_json_paths):
    res = []
    for json_path in table_json_paths:
        json_data = _safe_get_object_from_path(page_data, json_path)

        if not type(json_data) is list:
            logger.warn('node is not a list')
            return None

        res = res + json_data
    return res

def _put_json_object():
    pass

def scrape_eqt_page(
    app_config: AppConfig,
    page_config: EqtWebTableScraperConfig
):
    page_data = _get_page_data_json(page_config.data_url)

    if not page_data:
        raise ScrapingException('Could not get page_data')

    print(_collect_and_validate_table_rows(page_data, page_config.json_data_paths))
