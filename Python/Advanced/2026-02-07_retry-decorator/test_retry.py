import pytest
from solution_retry import funcion_1

@pytest.mark.parametrize("esperado",
                         [(ValueError), (ValueError), ("OK")])
def test_funcion_1(esperado):
    assert funcion_1() == esperado
    assert funcion_1() == esperado
    assert funcion_1() == esperado