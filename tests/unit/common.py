import pytest

from common import get_first_year


@pytest.mark.parametrize('year', [
    1971, 1932, 1923, 1910, 2001, 2009
])
def test_get_first_year(year):
    start = get_first_year(year)
    assert str(start)[-1] == '0'
