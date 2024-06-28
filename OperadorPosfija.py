def procesaUnOperador(pilaOperando, op):
    op1 = pilaOperando.pop()
    op2 = pilaOperando.pop()
    if(op=="+"):
        pilaOperando.append(op1+op2)
    elif(op=="-"):
        pilaOperando.append(op1-op2)
    elif(op=="*"):
        pilaOperando.append(op1*op2)
    elif(op=="/"):
        pilaOperando.append(op1/op2)
    elif(op=="^"):
        pilaOperando.append(op1**op2)


def evaluarExpresion(expPosfija, listaVal):
    pilaOperando=[]
    for letra in expPosfija:
        if(letra=="+" or letra =="*" or letra == "/" or letra == "^" or letra == "-"):
            procesaUnOperador(pilaOperando, letra)
        else:
            pilaOperando.append(listaVal[letra])