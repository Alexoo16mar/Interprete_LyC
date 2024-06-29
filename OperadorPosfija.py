from AutomataPila import MiExcepcion
def procesaUnOperador(pilaOperando, op):
    op2 = pilaOperando.pop()
    op1 = pilaOperando.pop()
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
    return pilaOperando


def evaluarExpresion(lista_tokens, lista_simbolos):
    pilaOperando = []
    for token in lista_tokens:
        if token.get_tipo()=="<Operador_Aritmetico>":
            pilaOperando=procesaUnOperador(pilaOperando, token.get_dato())
        elif token.get_tipo()=="Numerico":
            pilaOperando.append(token.get_valor())
        elif token.get_tipo()=="ID":
            if token.get_dato() in lista_simbolos:
                # Si la variable ya ha sido declarada
                pilaOperando.append(lista_simbolos[token.get_dato()])
            else:
                raise MiExcepcion("La variable " + token.get_dato() + " no ha sido declarada")
    return pilaOperando.pop()