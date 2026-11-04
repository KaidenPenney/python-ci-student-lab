import pytest
from main import add


# Ensure there are two blank lines above the test function
def test_add():
    assert add(2, 3) == 5
