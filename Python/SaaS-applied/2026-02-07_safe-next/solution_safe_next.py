# Hay primero que ver las partes de las que se compone una url

from urllib.parse import urlsplit, urlparse

def is_safe_next(next_url): #Se pasa solo la url_next, es decir a partir de la query de la completa

    if next_url is None:
        return False

    lineas_partidas=str(next_url).splitlines()
    if len(lineas_partidas)>=2:
        return False

    next_url="".join(lineas_partidas).strip()


    extensiones_dominio_maligno=["com", "es", "dio", "dev", "mx", "net", "org", "info", "xyz", "co", "ai", "io", "app", "tech"]
                       

    try:
        url_parseada=urlsplit(next_url, allow_fragments=True)
    except ValueError:  # e.g. invalid IPv6 addresses
        return False
    
    if len(next_url)>2048:
        return False


    protocolo=url_parseada.scheme
    netloc=url_parseada.netloc  #Incluye el puerto, pero no debería tener la next_url
    path=url_parseada.path
    query=url_parseada.query    #Aquí se deben encontrar los parámetros
    fragment=url_parseada.fragment

    if protocolo!="": #Si no esta vacio, lo mismo que poner scheme!=""
        if protocolo[0]=="C":  #Si empieza por C no es relativa la ruta y no se permite
            return False

    if protocolo or netloc:
        return False    #No es segura
    
    if next_url=="":
        return False #Ruta cons String vacío
        

    if path.startswith("/") and not path.startswith("//"):
        try:
            num=path.count(".")
            if num:
                if str(path).split(".")[num] in extensiones_dominio_maligno:
                    return False
                
            if "\\" in path:    #Relmente es la forma de poner una linea "\"
                return False
            
        except TypeError:
            return True
        
        return True
    
    return False
        
