
Plans={"FREE":0, "PRO":19, "PREMIUM": 49}

class Errores(Exception):   #Hereda de Exception, para poder crear el error personalizado

    def error_not_found(update):
        raise Errores(f"No existe el plan {update} ")

    
    

class User():


    def __init__(self, email, plan="FREE"):
        self.email=email
        self.plan=plan.upper()
        

    @property
    def actualplan_get(self):
        return self.plan
    
    @staticmethod
    def input_clean(input_update):
        while True:
            try:
                update=str(input_update).upper()
                if update not in Plans.keys():
                    raise Errores(update)
                
                break

            except ValueError:
                input_update=input("Introduce un update correcto (FREE, PRO, PREMIUM): ").strip().upper()   #Importante que se llame igual que la entrada para
                                                                                                            #que la cambie en caso de fallo                
    
            except Errores as e:
                print(e)
                input_update=input("El plan que quieres selecionar no existe prueba (FREE, PRO, PREMIUM): ").strip().upper()
                

        return update
    

    def update_plan(self, update):

        update_limpio=User.input_clean(update)

        if str(self.plan).upper() in Plans.keys():
            if self.price_actual_plan() < Plans[update_limpio.upper()]:    #Puede romperse si sobre update no metemos un string pero la idea del ej no es hacer
                self.plan = update_limpio                            #Otra func para validar la entrada
                return self.price_actual_plan()
            
            return "No puedes cambiar a un plan peor o igual"
            
        return "Error, plan actual es no existente"     #Estos returns solo se visualizan con print en la llamada a la función a partir de la instancia del objeto o clase


    def price_actual_plan(self):
        return Plans[self.plan]
    




Mario=User("kartingcroc@gmail.com", "Pro")


print(Mario.update_plan(1))


    



        

    