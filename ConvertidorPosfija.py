import Token as tk
import OperadorPosfija as Op

def prioridadExp(x):
    if x == "^":
        return 4
    elif x == "*" or x == "/":
        return 2
    elif x == "+" or x == "-":
        return 1
    elif x == "(" or x == ")":
        return 5
    else:
        return 0

def prioridadPila(x):
    if x == "^":
        return 3
    elif x == "*" or x == "/":
        return 2
    elif x == "+" or x == "-":
        return 1
    elif x == "(" or x == ")":
        return 0
    else:
        return 0

def esOperador(letra):
    if letra == "+" or letra == "-" or letra == "*" or letra == "/" or letra == "^" or letra == "(" or letra == ")":
        return True
    else:
        return False

def conversionPosfija(lista_tokens):
    lista_posFija = []
    pila = []
    for token in lista_tokens:
        letra = token.get_dato()
        if esOperador(letra):
            if letra == ")" and len(pila) != 0:
                while pila[-1].get_dato() != "(":
                    lista_posFija.append(pila.pop())
                if pila[-1].get_dato() == "(":
                    pila.pop()
            if len(pila) == 0 and letra != ")":
                pila.append(token)
            elif letra != ")":
                pe = prioridadExp(letra)
                pp = prioridadPila(pila[-1].get_dato())
                if pe > pp:
                    pila.append(token)
                else:
                    lista_posFija.append(pila.pop())
                    pila.append(token)
        else:
            lista_posFija.append(token)
    while len(pila) != 0:
        lista_posFija.append(pila.pop())
    return lista_posFija

