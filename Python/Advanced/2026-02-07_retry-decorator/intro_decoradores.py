


def saludar_operación(func):

    print(f"Buenas voy a realizar la operación {func.__name__} y su suma {func(x=7, y=8)}") #Se comprueba que tengo que pasarle los valores {func} no vale
    return func                                                                             #si solo paso func recibo objeto la instancia pues no se dan valores



@saludar_operación
def sumar(x, y):

    while True:     #Mejor hacerlo así que con el .isinteger() que se rompe el código a la mínima
        try:
            x=float(x)
            break

        except ValueError:
            x=float(input("Introduce el número 1 de forma correcta: "))

    while True:
        try:
            y=float(y)
            break

        except ValueError:
            y=float(input("Introduce el número 2 de forma correcta: "))
    
    return x + y

print(sumar(3, 2))



def saludar_operacion_robusta(func):

    def wrapper(*args, **kwargs):

        resultado=func(*args, **kwargs) #Coge cualquier valor, o diccionario de valores, en este caso las dos entradas que introduzcamos, para poder pasarlo a la función
        print(f"Vamos a realizar la operación {func.__name__}, cuyo resultado es {resultado}")  #Esta es la gracia de la función que hemos llamado envoltorio

    return wrapper  #Para que así se ejecute la función wrapper


@saludar_operacion_robusta
def sumar_2(x, y):

    while True:     #Mejor hacerlo así que con el .isinteger() que se rompe el código a la mínima
        try:
            x=float(x)
            break

        except ValueError:
            x=float(input("Introduce el número 1 de forma correcta: "))

    while True:
        try:
            y=float(y)
            break

        except ValueError:
            y=float(input("Introduce el número 2 de forma correcta: "))
    
    return x + y



sumar_2(6, 8)   #He vuelto a crear la función solo para poder mostrar el otro decorador



#Varias formas de utilizar las instancias de los objetos

def doble_numero_instanciada(num):  #Recibe el número de la función ya instanciada
    return 2*num


resultado=doble_numero_instanciada(sumar(10, 15))   #Aquí directamente paso el resultado
print(resultado)


def doble_numero_referencia(func):  #Podría ponerlo como decorador, no lo hago porque ya tiene una esa función
    valor_func=func(10, 15)
    return valor_func * 2


resultado=doble_numero_referencia(sumar)
print(resultado)


def doble_numero_params(func):  #También sirve el decorador, paso la función con los parametros
    resultado=func()
    return resultado * 2

print(doble_numero_params(lambda: sumar(10,15)))    #Sin lambda me va a dar error puede comprobarse, no se pasan los parámetros a la instancia interna
