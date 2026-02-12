

def retry(max_tries):   #Recibe los parametros del decorador

    def decorador_apoyo(func):    #Recibe la función

        def fun_envoltorio(*args, **kwargs):    #Recibe cualquier valor (lógica) para cualquier función válido
            i=0
            while i < max_tries:
                try:
                    i+=1
                    valor=func(*args,**kwargs)  #Coge los valores de la funcion_1
                    print(f"Funciono en el intento {i}")
                    return valor

                except Exception as e:
                    print(f"Fallo en el intento{i}")
                    last_exception=e
            
            print(f"Se agotaron los intentos totales {i}")
            raise last_exception #Se lanza al final
                
        return fun_envoltorio      

    return decorador_apoyo



def crear_func_x_veces(x):
    dic={"Contador":0}  #Para poder definir el contador y que inice en 0, pero cada pasada no se resetee a 0, podría ser un simple i

    @retry(max_tries=3)
    def falla_x_veces():   #Debería limitar max_tries que ejecuta la funcion
        dic["Contador"]+=1
        
        if dic["Contador"] <= x:
            raise ValueError    #Error cualquiera de prueba

        return "OK"

    return falla_x_veces



#Fallo 2 veces la 3era funciona
f = crear_func_x_veces(2)
print(f())

#Siempre falla
f = crear_func_x_veces(6)
#print(f())


"""Este ejercicio se ha simuldo que por ejemplo una api falla x veces por razones desconocidas por ejemplo sobrecarga del servidor, pero se vuelve a lanzar y 
acaba corriendo o no.   Se ha utilizado ValueError a modo de prueba, podría usarse el propio del manejo de errores de esa función, o el general que recoge todo"""