from solution_upgrade_plan import User_tests, Errores
import pytest

@pytest.mark.parametrize("email ,update",
                         [("lobato@gmail.com", "Pro"),
                          ("lobato@gmail.com", "PRO")])
def test_User_Plan(email, update):
    Usuario=User_tests(email)
    assert Usuario.update_plan(update) == 19




Usu_creado=User_tests(email="estebanez@email.net")
Usu_creado.update_plan(update="PRO")

@pytest.mark.parametrize("usuario, update",
                         [(Usu_creado, "FREE"), (Usu_creado, "PRO")])
def test_User_Plan_Inferior_Igual(usuario, update):
    assert usuario.update_plan(update)=="No puedes cambiar a un plan peor o igual"


@pytest.mark.parametrize("email, update_num",
                         [("lcoc8@gamil.com", 1)])
def test_update_invalido(email, update_num):
    Usuario=User_tests(email)
    assert Usuario.update_plan(update_num) == "Plan inválido o la entrada debe ser string"