import pytest

from lib.models.EqtWebTableScraperConfig import EqtWebTableScraperConfig


@pytest.mark.parametrize(
    'dict_in',
    [
        { 'table_name': '', 'page_data_path': ['b'], 'json_data_paths': [[['c']]], 'columns': ['d'] },
        { 'table_name': 'a', 'page_data_path': [], 'json_data_paths': [['c']], 'columns': ['d'] },
        { 'table_name': 'a', 'page_data_path': ['b'], 'json_data_paths': [], 'columns': ['d'] },
        { 'table_name': 'a', 'page_data_path': ['b'], 'json_data_paths': 'asd', 'columns': ['d'] },
        { 'table_name': 'a', 'page_data_path': ['b'], 'json_data_paths': ['c'], 'columns': ['d'] },
        { 'table_name': 'a', 'page_data_path': ['b'], 'json_data_paths': [['c']], 'columns': [] },
        { 'table_name': 'a', 'page_data_path': ['b'], 'json_data_paths': [['c']], 'columns': 'asd' },
        { 'page_data_path': ['b'], 'json_data_paths': [['c']], 'columns': ['d'] },
        { 'table_name': 'a', 'json_data_paths': [['c']], 'columns': ['d'] },
        { 'table_name': 'a', 'page_data_path': ['b'], 'columns': ['d'] },
        { 'table_name': 'a', 'page_data_path': ['b'], 'json_data_paths': [['c']] }
    ]
)
def test_missing_config_raises_value_error(dict_in):
    with pytest.raises(ValueError):
        EqtWebTableScraperConfig.from_dict(dict_in)

def test_valid_config_is_parsed():
    dict_in = {
        'table_name': 'a',
        'page_data_path': ['b'],
        'json_data_paths': [['c']],
        'columns': ['d']
    }

    res = EqtWebTableScraperConfig.from_dict(dict_in)

    assert res.table_name == dict_in['table_name']
    assert res.page_data_path == dict_in['page_data_path']
    assert res.json_data_paths == dict_in['json_data_paths']
    assert res.columns == dict_in['columns']
