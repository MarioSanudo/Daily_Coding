raw_sessions = [
    {"user": "mario", "duration_min": 45, "avg_power": 210, "valid": True},
    {"user": "ana",   "duration_min": 0,  "avg_power": 180, "valid": True},
    {"user": "luis",  "duration_min": 30, "avg_power": None, "valid": True},
    {"user": "mario", "duration_min": 60, "avg_power": 250, "valid": True},
    {"user": "ana",   "duration_min": 20, "avg_power": 195, "valid": False},
    {"user": "luis",  "duration_min": 55, "avg_power": 230, "valid": True},
    {"user": "mario", "duration_min": 10, "avg_power": 170, "valid": True},
]



def filter_valid(list_dic_session):
    list_dic_session_helper=list_dic_session.copy()

    for dic_session in list_dic_session_helper:   #Si lo borro de la misma lista, cambia el orden y me salta elementos

        match dic_session:

            case {"duration_min": time, "avg_power": power, "valid":True} if power is not None and time>0:
                pass
    
            case _:
                list_dic_session.remove(dic_session)    #Con indices da problema al andar borrando en el momento el dic, lo mismo pasaría con la lista
    
    return  list_dic_session
            
        
    
def normalize_session(list_dic_session):
    for dic_session in list_dic_session:
        match dic_session:
            
            case {"avg_power": power} if power>=220:
                dic_session["intensity"]="high"
            
            case {"avg_power": power} if 180<=power<=220:
                dic_session["intensity"]="medium"

            case _:
                dic_session["intensity"]="low"
            
    return list_dic_session



def group_by_user(list_dic_session):
    name_list=[]
    users_name_dic={}

    for dic_session in list_dic_session:

        match dic_session:

            case {"user": nombre} if nombre in name_list:
                users_name_dic.setdefault(str(nombre),[]).append(dic_session)
            
            case _:
                users_name_dic[str(nombre)]=[dic_session]
        
        name_list.append(dic_session["user"])
        
    return users_name_dic



def sumarize_user(users_name_dic):

    lista_users_sum=[]

    for user_dic_list in users_name_dic.values():
        total_minutes=0
        avg_power=0
        
        total_sessions=int(len(user_dic_list))

        for user_dic in user_dic_list:

            total_minutes+=user_dic["duration_min"]
            avg_power+=float(user_dic["avg_power"])
        
        sum_user_dic={"total_sessions": total_sessions, "avg_power": avg_power/total_sessions, "total_minutes": total_minutes}
        lista_users_sum.append(sum_user_dic)
        
    return lista_users_sum

            
"""
def filter_valid_con_if(dic_session):       #Más limpio con el match y el case

    for i, session in enumerate(dic_session):
        
        time=session["duration_min"]
        valid=session["valid"]
        analysis=session["avg_power"]

        if valid and analysis and time>0:           
            print("Es correcto")
            continue

        dic_session.pop(i)

    return dic_session      #No hago manejo de errores porque ya se me ha pasado la lista el ejercico y se que no necesito validarla
"""



if __name__=="__main__":

    list_dic_session=filter_valid(raw_sessions)
    normalize_list_dic_session=normalize_session(list_dic_session)
    users_name_dic=group_by_user(normalize_list_dic_session)
    sumarize_users=sumarize_user(users_name_dic)
    print(sumarize_users)
