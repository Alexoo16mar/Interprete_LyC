def prioridadExp(x):
    if(x=="^"):
        return 4
    elif(x=="*" or x=="/"):
        return 2
    elif(x=="+" or x=="-"):
        return 1
    elif(x=="(" or x==")"):
        return 5
    else:
        return 0

def prioridadPila(x):
    if(x=="^"):
        return 3
    elif(x=="*" or x=="/"):
        return 2
    elif(x=="+" or x=="-"):
        return 1
    elif(x=="(" or x==")"):
        return 0
    else:
        return 0

def esOperador(letra):
    if(letra=="+" or letra=="-" or letra=="*" or letra=="/" or letra=="^" or letra=="(" or letra==")"):
        return True
    else:
        return False

def conversionPosfija(expInf):
    lista_posFija=[]
    pila=[]
    for letra in expInf:
        if(esOperador(letra)):
            if(letra==")" and len(pila)!=0):
                while(pila[-1]!="("):
                    lista_posFija.append(pila.pop())
                if(pila[-1]=="("):
                    pila.pop()
            
            if(len(pila)==0):
                if(letra!=")"):
                    pila.append(letra)
            else:
                if(letra!=")"):
                    pe=prioridadExp(letra)
                    pp=prioridadPila(pila[-1])
                    if(pe>pp):
                        pila.append(letra)
                    else:
                        lista_posFija.append(pila.pop())
                        pila.append(letra)
        else:
            lista_posFija.append(letra)
    
    while(len(pila)!=0):
        lista_posFija.append(pila.pop())
    return lista_posFija

expInfija="x*y-(z+w)/(z+y)^x"
expPosfija=conversionPosfija(expInfija)
print(expPosfija)
