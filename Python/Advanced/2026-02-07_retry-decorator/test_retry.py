import pytest
from solution_retry import crear_func_x_veces


def test_siempre_falla():   #También el nombre de la función aparte del fichero tiene que ser test_"algo"
    f=crear_func_x_veces(5)

    with pytest.raises(ValueError):
        f()
        
        
def test_falla_final():
    f=crear_func_x_veces(2)

    assert f()=="OK"