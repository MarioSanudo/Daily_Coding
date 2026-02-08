#1
def word_freq(texto):
    lista=[]
    dic={}

    if texto:
        dividido=str(texto).lower().splitlines()    #Por si hay saltos de línea
        
        limpiado=" ".join(dividido)
        for c in limpiado:
            if c.isalnum(): 
                lista.append(c)
            elif not c.isalnum():
                lista.append(" ")   #Que añada también los espacios
                

        palabras="".join(lista).split() #Separa por espacios de serie, colapsa espacios, saltos, tabs
        for palabra in palabras:    #Ahora recorremos una lista no un string

            if palabra in dic:
                dic[palabra]+=1
            else:
                dic[palabra]=1

    return dic
    


