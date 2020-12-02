import pytest

from vivo.ex01.get_an import get_an


@pytest.fixture
def normal_entry():
    return list(range(16))


@pytest.fixture
def empty_list():
    return []


def test_get_an(normal_entry):
    result = get_an(normal_entry)
    assert (
        result
        == '{0: 1, 1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1, 10: 1, 11: 1, 12: 1, 13: 1, 14: 1, 15: 1}'
    )


def test_get_an_empty(empty_list):
    result = get_an(empty_list)
    return (
        result
        == '{0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0, 13: 0, 14: 0, 15: 0}'
    )


def test_get_different_values():
    result = get_an([1, 3, 5, 5, 5, 6, 7, 8, 15, 13, 12, 13, 15, 10, 2, 2, 11, 11, 11])
    assert (
        result
        == '{0: 0, 1: 1, 2: 2, 3: 1, 4: 0, 5: 3, 6: 1, 7: 1, 8: 1, 9: 0, 10: 1, 11: 3, 12: 1, 13: 2, 14: 0, 15: 2}'
    )


def test_get_wrong_values(caplog):
    get_an([1, 3, 5, 5, 5, 6, 7, 8, 15, 13, 12, 13, 15, 17, 18, 19])
    assert 'Number should be between 0 and 15' in caplog.text
