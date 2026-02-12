from solution_context_manager import DB_connection
import pytest


@pytest.mark.parametrize("db_setting",
                         [({"host": "localhost",
                            "user": "root" ,           
                            "password": "Hm07052005" ,
                            "database": "entreno_chat-gpt-user-orders" })])
def test_db_conection_certero(db_setting):
    with DB_connection(db_setting) as db:
        assert db.execute_ext("select * from subscriptions") is True




@pytest.mark.parametrize("db_setting",
                         [({"host": "localhost",
                            "user": "root" ,           
                            "password": "Hm07052005" ,
                            "database": "entreno_chat-gpt-user-orders" })])
def test_db_conection_ERROR(db_setting):
    with DB_connection(db_setting) as db:
        assert db.execute_ext("select ERROR from subscriptions")=="Hola"
