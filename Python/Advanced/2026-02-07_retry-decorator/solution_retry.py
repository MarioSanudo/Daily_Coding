

def retry(max_tries):   #Recibe los parametros del decorador

    def decorador_apoyo(func):    #Recibe la función

        def fun_envoltorio(*args, **kwargs):    #Recibe cualquier valor (lógica) para cualquier función válido
            i=0
            while i <= max_tries:
                try:
                    i+=1
                    print(i)
                    resultado=func(*args,**kwargs)
                    return resultado
        
                except Exception as e:
                    retry  
                
        return fun_envoltorio      

    return decorador_apoyo


@retry(max_tries=3)
def funcion_1(*i):   #Coge el valor de los args
    texto="Paco"
    if i==1:
        var=float(texto) #Fallo provocado
    
    elif i==2:
        var=int(texto)

    elif i==3:
        var=texto.split()   #Esto ya es correcto

    return var

funcion_1()