from typing import List

class EqtWebTableScraperConfig:

    def __init__(
        self,
        name,
        data_url: str,
        json_data_paths: List[List[str]],
        columns: List[str]
    ):
        if not name:
            raise ValueError('Missing name')
        if not data_url:
            raise ValueError('Missing data_url')
        if not json_data_paths or type(json_data_paths) is not list or not all(type(p) is list for p in json_data_paths):
            raise ValueError('json_data_paths must be a non-empty list of data paths')
        if not columns or type(columns) is not list:
            raise ValueError('columns must be a non-empty list')

        self.data_url = data_url
        self.json_data_paths = json_data_paths
        self.columns = columns

    @classmethod
    def from_dict(cls, name, config_dict):
        return cls(
            name=name,
            data_url=config_dict['data_url'],
            json_data_paths=config_dict['json_data_paths'],
            columns=config_dict['columns']
        )
