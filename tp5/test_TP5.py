import pytest
from funciones import *

@pytest.mark.parametrize("a, b, c, res",[
    ("Nicolas Federico", "Willemet", 42914807, "Nicolas8429")
    ("Juan José", "Roca", 26945623, "Juan4269")
])
def test_identifier(a, b, c, res):
    assert identifier(a,b,c) == res
