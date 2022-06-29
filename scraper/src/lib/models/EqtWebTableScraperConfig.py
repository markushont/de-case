from typing import List

class EqtWebTableScraperConfig:

    def __init__(
        self,
        table_name,
        page_data_path: str,
        json_data_paths: List[List[str]],
        columns: List[str]
    ):
        if not table_name:
            raise ValueError('Missing name')
        if not page_data_path:
            raise ValueError('Missing page_data_path')
        if not json_data_paths or type(json_data_paths) is not list or not all(type(p) is list for p in json_data_paths):
            raise ValueError('json_data_paths must be a non-empty list of data paths')
        if not columns or type(columns) is not list:
            raise ValueError('columns must be a non-empty list')

        self.table_name = table_name
        self.page_data_path = page_data_path
        self.json_data_paths = json_data_paths
        self.columns = columns

    @classmethod
    def from_dict(cls, config_dict):
        return cls(
            table_name=config_dict['table_name'],
            page_data_path=config_dict['page_data_path'],
            json_data_paths=config_dict['json_data_paths'],
            columns=config_dict['columns']
        )
