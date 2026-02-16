import pytest
from solution_Users_Fundamentals import User, User_Manager


@pytest.fixture
def email():
    email="ka@gmail.com"
    return email


def test_Usuario_texto(email):

    usuario=User(email)
    assert usuario == "No se va a instanciar un objeto que no cumple los requisitos"



def test_email_corto(email):
    
    valor=User.email_checker(email)

    assert valor == "El email no cumple la longitud mínima de 5 caracteres"




@pytest.mark.parametrize("email_input",
                         ["kartingcroc@gmail.com"])
def email_correcto(email_input):
    assert User.email_checker(email_input) is True




@pytest.mark.parametrize("email_input",
                         ["kartingcroc"])
def email_incorrecto(email_input):
    
    assert User.email_checker(email_input) == "El email no cumple el formato mínimo"



@pytest.mark.parametrize("email_input",
                         [(1)])
def email_invalido(email_input):
    assert User.email_checker(email_input) is AttributeError