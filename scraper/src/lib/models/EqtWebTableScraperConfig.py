from typing import List

class EqtWebTableScraperConfig:

    def __init__(
        self,
        name,
        data_url: str,
        json_data_path: List[str],
        columns: List[str]
    ):
        if not name:
            raise ValueError('Missing name')
        if not data_url:
            raise ValueError('Missing data_url')
        if not json_data_path or type(json_data_path) is not list:
            print(json_data_path)
            raise ValueError('json_data_path must be a non-empty list')
        if not columns or type(columns) is not list:
            raise ValueError('columns must be a non-empty list')

        self.data_url = data_url
        self.json_data_path = json_data_path
        self.columns = columns

    @classmethod
    def from_dict(cls, name, config_dict):
        return EqtWebTableScraperConfig(
            name=name,
            data_url=config_dict['data_url'],
            json_data_path=config_dict['json_data_path'],
            columns=config_dict['columns']
        )
