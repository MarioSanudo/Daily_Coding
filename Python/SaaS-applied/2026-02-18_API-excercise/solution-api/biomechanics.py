

#inseam es longitud entrepierna
def valid_inseam_cm(inseam_cm):
    try:
        inseam_cm=float(inseam_cm)
        if inseam_cm not in range(50, 120):
            raise ValueError
        
        return inseam_cm
    
    except ValueError as e:
        raise e


def valid_method(method):

    if method.lower().strip() == ("lemond" or "hamley"):
        return method.lower().strip()
    
    return None



def calculate_saddle_height(inseam_cm, method):

    inseam_cm=valid_inseam_cm(inseam_cm)
    method=valid_method(method)

    print(method)

    if method == "lemond":
        saddle_height= inseam_cm * 0.883
    
    elif method == "hamley":
       saddle_height= (inseam_cm * 1.09) - 10.16
    
    else:
        raise ValueError
    
    return {"saddle_height":saddle_height, "method": method, "inseam_cm": inseam_cm }


    

    
    
