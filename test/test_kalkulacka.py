import pytest
#from code.kalk import *
from kalk import Kalkulacka
import math

@pytest.fixture
def calculator():
    return Kalkulacka()


@pytest.mark.parametrize("a,b,out", [
    (1, 2, 3),
    (-1, -2, -3),
    (5, -7, -2)
])
def test_plus(a, b, out, calculator):
    assert calculator.plus(a,b) == out
    

def test_posledni_vysledek(calculator):
    calculator.plus(3, 2)
    assert calculator.posledni_vysledek() == 5



@pytest.mark.parametrize("x,out", [
    (0, 0),
    (math.pi / 2, 1),
    (3 * math.pi / 2, -1)
])
def test_sin(x,out,calculator):
    assert calculator.sin(x) == out