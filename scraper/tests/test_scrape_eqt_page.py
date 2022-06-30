
import pytest
from scrape_eqt_page import _safe_get_object_from_path


@pytest.mark.parametrize(
    ['dict_in', 'path', 'out'],
    [
        ({'a': {'b': 1}}, ['a'], {'b': 1}),
        ({'a': 1}, ['a'], 1),
        ({'a': {'b': 1}}, ['a', 'b'], 1),
        ({'a': {'b': 1}}, ['c'], None)
    ]
)
def test__safe_get_object_from_path(dict_in, path, out):
    res = _safe_get_object_from_path(dict_in, path)

    assert res == out


# TODO: More tests with mocked requests module
