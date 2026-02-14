import mysql.connector

class Db_connection_prueba():  #Simulación funcionamiento conexión base de datos

    def __enter__(self):
        print("Conexión abierta")
        return self

    def __exit__(self, excepcion_tipo, excepcion_contenido, excepcion_traceback):    #Se devuelven estos 3 parámetros si hubo algún error

        if excepcion_tipo is not None:
            print(f"Significa que has tenido el error {excepcion_contenido} cuyo traceback es {excepcion_traceback}")

        return True #Devuelvo cualquier cosa para que no se devuelva el error quue lance en la la función execute
    
    @staticmethod
    def execute(query):

        texto_query=str(query).upper()

        if "ERROR" in texto_query:
            raise ValueError("Query Inválida")
        
        print({"Ejecutando": {query}})
    
    

#Ejemplo más complejo simulando la conexión a una base de datos de verdad

class DB_connection():

    

    def __init__(self, db_config):   #Self es la instancia de la base de datos en este ejemplo
    
        self.config=db_config
        self.connection=None   #Todas los atributos que necesitaré para trabajar alrededor de la clase
        self.cursor=None


    def __enter__(self):

        try:
            if self.config:
                self.connection=mysql.connector.connect(**self.config)  #El ** del diccionario lo separa en keys:values, para poder configurar, es más
                return self                                             #legible si se escribe a mano

            else:
                raise ConnectionAbortedError
        
        except ConnectionAbortedError as e:
            raise e
        
        except mysql.connector.errors.ProgrammingError as e:
            raise e
        
        except mysql.connector.Error as e:
            raise e
        


    def __exit__(self, excepcion_tipo, excepcion_contenido, excepcion_traceback):   #Aquí se recogen los errores

        

        try:
            if excepcion_tipo is None:
                print("No ha habido errores la base de datos se ha conectado correctamente")
                self.connection.commit()  
                #Para evitar que se devuelva el error
            
            else:
                print(f"Ha ocurrido el siguiente error {excepcion_tipo.__name__}, {excepcion_contenido}")
                self.connection.rollback()  #Otro rollback por si acaso

        finally:
            self.cursor.close()
            self.connection.close()

            print("Hecho todo esta cerrado")

        
        return False #Evita truthy, si hay error se lanza si no hay error no se lanza nada y se ejecuta correctamente, ver como si se pone True, no hay error
                     #en la consola aunque la sintaxis de SQL mal escrita

    
   
    def execute_ext(self, execute): #Se ejecuta después del __enter__ ya existe conexión

        self.cursor=self.connection.cursor()
        try:
            query_limpia=str(execute).upper().strip()

            if query_limpia:
                self.cursor.execute(query_limpia)
                rows=self.cursor.fetchall()
                
                for i, row in enumerate(rows):

                    print(f"Fila {i} contiene {row}")
                
                return True #Si todo va ok

            raise ValueError
        
        except ValueError as e:
            raise e
        
        except mysql.connector.errors.ProgrammingError as e:
            raise e

        except mysql.connector.Error as e:
            self.connection.rollback()  
            raise e



if __name__=="__main__":

    db_config={
            "host": "localhost",
            "user": "root" ,            #La función connect reconoce el json y lo implementa
            "password": "Hm07052005" ,
            "database": "entreno_chat-gpt-user-orders" 
        }

    with DB_connection(db_config) as db:

        db.execute_ext("select * from subscriptions")



    #Test con prints
    def test_db_connection_debug(db_setting):
        with DB_connection(db_setting) as db:
            resultado_ok = db.execute_ext("SELECT * FROM subscriptions")
            resultado_error = db.execute_ext("SELECT ERROR FROM subscriptions")
            
            print("\n=== DIAGNÓSTICO ===")
            print(f"Resultado OK: {resultado_ok}")
            print(f"Tipo OK: {type(resultado_ok)}")
            print(f"Resultado ERROR: {resultado_error}")
            print(f"Tipo ERROR: {type(resultado_error)}")
            print(f"resultado_ok is True: {resultado_ok is True}")
            print(f"resultado_error is None: {resultado_error is None}")


    test_db_connection_debug(db_config)