import pytest
from home_work.hw_1.simple_match import Simple_match


@pytest.fixture
def match():
    """Fixture для создания объекта Simplematch"""
    return Simple_match()


def test_square(match):
    """Тест метода square"""
    assert match.square(2) == 4
    assert match.square(-3) == 9
    assert match.square(0) == 0
    assert match.square(5) == 25


def test_cube(match):
    """Тест метода cube"""
    assert match.cube(2) == 8
    assert match.cube(-3) == -27
    assert match.cube(0) == 0
    assert match.cube(4) == 64
