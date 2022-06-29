from datetime import datetime
import requests
from lib.CloudStorageClient import CloudStorageClient

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

def _get_page_data_json(base_url, path):
    url = f"{base_url}{path}"
    res = requests.get(url=url)

    if not res.ok:
        logger.warn('Could not fetch url', extra={'url': url, 'status': res.status_code, 'response': res.text})

    return res.json() if res.ok else None

def _collect_and_validate_table_rows(page_data, table_json_paths, table_columns):
    res = []
    for json_path in table_json_paths:
        json_data = _safe_get_object_from_path(page_data, json_path)

        if not type(json_data) is list:
            logger.warn('node is not a list')
            return None

        for column in table_columns:
            for row in json_data:
                if not column in row:
                    logger.warn(f"Missing attribute {column}", extra={'row': row})

        res = res + json_data
    return res

def _enrich_with_timestamp(table_rows):
    return [
        {**r, '_fetched_time': datetime.utcnow().isoformat()}
        for r in table_rows
    ]

def _stringify_json(table_rows):
    # BigQuery doesn't handle object types :(
    return [
        {
            k: str(v) if type(v) is list or type(v) is dict else v for k, v in row.items()
        }
        for row in table_rows
    ]

def _put_json_object(app_config: AppConfig, file_name, table_rows):
    client = CloudStorageClient(project_id=app_config.gc_project_id,
        service_account_creds_dict=CloudStorageClient.credentials_from_app_config(app_config))

    client.put_newline_json(bucket=app_config.target_bucket, path=file_name, obj=table_rows)

def scrape_eqt_page(
    app_config: AppConfig,
    page_config: EqtWebTableScraperConfig
):
    page_data = _get_page_data_json(app_config.eqt_base_url, page_config.page_data_path)

    if not page_data:
        raise ScrapingException('Could not get page_data')

    table_rows = _collect_and_validate_table_rows(page_data=page_data,
        table_json_paths=page_config.json_data_paths, table_columns=page_config.columns)

    if not table_rows:
        logger.info('Table is empty, exiting')
        return

    table_rows = _stringify_json(table_rows)
    table_rows = _enrich_with_timestamp(table_rows)

    file_name = f"{page_config.table_name}/{datetime.utcnow().isoformat()}.json"
    _put_json_object(app_config, file_name, table_rows)
