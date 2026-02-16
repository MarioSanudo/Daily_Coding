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
def test_email_correcto(email_input):
    assert User.email_checker(email_input) is True




@pytest.mark.parametrize("email_input",
                         ["kartingcroc"])
def test_email_incorrecto(email_input):
    
    assert User.email_checker(email_input) == "El email no cumple el formato mínimo"



@pytest.mark.parametrize("email_input",
                         [1])
def test_email_invalido(email_input):
    with pytest.raises(AttributeError):
        assert User.email_checker(email_input)


"""
@pytest.fixture
def creacion_usuarios():
    lista_usuarios=[]
    email_1="kartingcroc@gmail.com";    email_2="mari2o@hotmail.com";   email_3="marito12@email.es"
    usu_1=User_Manager.add_user(email_1); usu_2=User_Manager.add_user(email_2); usu_3=User_Manager.add_user(email_3)
    lista_usuarios.append(usu_1, usu_2, usu_3)
    print(lista_usuarios)
    return lista_usuarios
    


def test_User_Manager_lengthl(creacion_usuarios):
    lista=creacion_usuarios()
    assert len(lista) == 3

"""