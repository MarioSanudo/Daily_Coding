from datetime import date, datetime


subscription_plans={"FREE": 0, "PRO": 15, "ENTERPRISE": 49} #No ponerlo dentro de la clase que sería atributo de clase o general


class User:

    def __new__(cls, email, subscription_tier:dict={"FREE": 0}):

        if User.email_checker(email) is True and User.subscription_tier_checker(subscription_tier.keys()) is True:
            return super().__new__(cls)
        
        return "No se va a instanciar un objeto que no cumple los requisitos"


    def __init__(self, email: str, created_at: datetime=datetime.now(), is_active: bool=True, subscription_tier: dict={"FREE": 0}):

        self._email= email
        self._subscription_tier= subscription_tier
        self._created_at= created_at
        self._is_active=is_active


    def __repr__(self):
        return f"Usuario {self._email}, subscripción {self._subscription_tier}, estando activo? {self._is_active}"
    
    
    @classmethod
    def email_checker(cls, email):
        while True:
            try:

                if not isinstance(email, str):
                    raise AttributeError
                
                if "." in email and "@" in email:
                    split_email=email.split(".")[0].split("@")[0].strip()
            
                    if len(split_email) < 5:
                        return "El email no cumple la longitud mínima de 5 caracteres"
                
                    return True

                return "El email no cumple el formato mínimo"


            except AttributeError as e:
                raise e("Tienes un número por email, mal")
            

    @property
    def email(self):
        return self._email  #Como getter para que sea inmutable
    
    @classmethod
    def subscription_tier_checker(cls, subscription):    #Si quitan la inicialización
        for sub in subscription:
            if sub in subscription_plans:
                return True
        return "Subscription tier actual inválido"
    

    def upgrade_subscription_tier(self, subscription_upgrade: str):

        try:

            if not isinstance(subscription_upgrade, str):
                raise AttributeError

            if subscription_upgrade.upper().strip() in subscription_plans.keys():

                for subscription_cost in self._subscription_tier.values():

                    if subscription_plans[subscription_upgrade] <= subscription_cost:
                        return "No puedes mejorar si no coges un plan superior"
                
                    self._subscription_tier = {subscription_upgrade:subscription_plans[subscription_upgrade]}
                    return self
                
            return "El plan que buscas no existe"
                 
        except AttributeError:
            raise AttributeError("El plan que se leccionas tiene que ser texto (string)")
    


    def get_account_age_days(self):

        lista=str(self._created_at).split("-")

        if len (lista) == 3 and len(lista[0]) == 4: #Para que empieze por el año

            current_year=date.today().year;     current_month=date.today().month;       current_day=date.today().day
            created_year=int(lista[0]);         created_month=int(lista[1]);            created_day=int(lista[2].split()[0])

            year_days=(created_year-current_year)*365;  month_days=(created_month-current_month)*30 ;   days=created_day-current_day
            total_days=year_days+ month_days+ days

            if total_days < 0:
                return f"La fecha que se introdució para el usuario {self.email} es errónea"
            
            return int(total_days)
        
        return "El formato de fecha de creación no es correcto"


if __name__=="__main__":
        
        Mario=User("kartingcroc@gmail.com")
        print(Mario)
        print(Mario.get_account_age_days())
        Mario.upgrade_subscription_tier("PRO")
        print(Mario._subscription_tier)

        Gustavo=User("gus@gmail.com")
        print(Gustavo)
            
 
    
#Parte del código se ha quedado algo enrebesado por el problema de tener que sacar el .keys(), o .values() del la lista que devuelve el metodos de dic
#No lo había previsto y por eso no creé una función para mantenerlo más ordenado
        

