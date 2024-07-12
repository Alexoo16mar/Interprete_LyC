from collections import deque
from Token import Token

class MiExcepcion(Exception):
    def __init__(self, mensaje):
        self.mensaje = mensaje

def AutomataPilaEA(lista_tokens):
    indicador = False
    indice = 0
    pila = deque()
    estado_actual = "q0"
    while estado_actual != "qf" and indice <= len(lista_tokens):
        if estado_actual == "q0":
            if lista_tokens[indice].get_tipo() == "ID":
                estado_actual = "q1"
                indice += 1
            else:
                raise MiExcepcion("Error! >> Expresion Incorrecta")
        if estado_actual == "q1":
            if indice == len(lista_tokens):
                estado_actual = "qf"
                indicador = True
            elif lista_tokens[indice].get_dato() == "=":
                estado_actual = "q2"
                indice += 1
            else:
                raise MiExcepcion("Error! >> Expresion Incorrecta")
        if estado_actual == "q2":
            if lista_tokens[indice].get_tipo() == "ID" or lista_tokens[indice].get_tipo() == "Numerico":
                estado_actual = "q3"
                indice += 1
            elif lista_tokens[indice].get_dato() == "(":
                estado_actual = "q5"
                indice += 1
                pila.append("(")
            else:
                raise MiExcepcion("Error! >> Expresion Incorrecta")
        if estado_actual == "q3":
            if indice == len(lista_tokens) and len(pila) == 0:
                estado_actual = "qf"
                indicador = True
            elif lista_tokens[indice].get_dato() == ")":
                if len(pila) == 0:
                    raise MiExcepcion("Error! >> Expresion Incorrecta")
                else:
                    pila.pop()
                estado_actual = "q3"
                indice += 1
            elif lista_tokens[indice].get_tipo() == "<Operador_Aritmetico>":
                estado_actual = "q8"
                indice += 1
            else:
                if len(pila)>0:
                    raise MiExcepcion("Error! >> Se espera un operador aritmetico")
                raise MiExcepcion("Error! >> Expresion Incorrecta")
        if estado_actual == "q5":
            if lista_tokens[indice].get_tipo() == "Numerico" or lista_tokens[indice].get_tipo() == "ID":
                estado_actual = "q6"
                indice += 1
            else:
                raise MiExcepcion("Error! >> Expresion Incorrecta")
        if estado_actual == "q6":
            if lista_tokens[indice].get_dato() == ")":
                estado_actual = "q3"
                pila.pop()
                indice += 1
            elif lista_tokens[indice].get_tipo() == "<Operador_Aritmetico>":
                estado_actual = "q7"
                indice += 1
            else:
                raise MiExcepcion("Error! >> Expresion Incorrecta")
        if estado_actual == "q7":
            if lista_tokens[indice].get_dato() == "(":
                estado_actual = "q5"
                pila.append("(")
                indice += 1
            elif lista_tokens[indice].get_tipo() == "Numerico" or lista_tokens[indice].get_tipo() == "ID":
                estado_actual = "q6"
                indice += 1
            else:
                raise MiExcepcion("Error! >> Expresion Incorrecta")
        if estado_actual == "q8":
            if lista_tokens[indice].get_dato() == "(":
                estado_actual = "q5"
                pila.append("(")
                indice += 1
            elif lista_tokens[indice].get_tipo() == "Numerico" or lista_tokens[indice].get_tipo() == "ID":
                estado_actual = "q3"
                indice += 1
            else:
                raise MiExcepcion("Error! >> Expresion Incorrecta")
    return indicador

# tokenprueba0 = Token("int", "tipo_var")
# tokenprueba1 = Token("a", "ID")
# tokenprueba2 = Token("=", "<Operador_asignacion>")
# tokenprueba3 = Token("5", "Numerico")
# tokenprueba32 = Token("+", "<Operador_Aritmetico>")
# tokenprueba33 = Token("2", "Numerico")
# lista= [tokenprueba0, tokenprueba1, tokenprueba2, tokenprueba3, tokenprueba32, tokenprueba33]
# try:
#     print(AutomataPilaEA(lista))
# except MiExcepcion as e:
#     print(e.mensaje)

# tokenprueba35 = Token("(", "-", "-", "-", "-", "")
# tokenprueba4 = Token("a", "ID", "-", "-", "-", "")
# tokenprueba5 = Token("+", "<Operador_Aritmetico>", "-", "-", "-", "")
# tokenprueba6 = Token("2", "Numerico", "-", "-", "-", "")
# tokenprueba7 = Token(")", "-", "-", "-", "-", "")
# tokenprueba72 = Token("*", "<Operador_Aritmetico>", "-", "-", "-", "")
# tokenprueba73 = Token("2", "Numerico", "-", "-", "-", "")
# tokenprueba75 = Token(")", "-", "-", "-", "-", "")

# lista_tokens = [
#     tokenprueba0, tokenprueba1, tokenprueba2, tokenprueba3, tokenprueba32, tokenprueba33,
#     tokenprueba35, tokenprueba4, tokenprueba5, tokenprueba6, tokenprueba7, tokenprueba72, tokenprueba73, tokenprueba75
# ]

# try:
#     print(AutomataPilaEA(lista_tokens))
# except MiExcepcion as e:
#     print(e.mensaje)


# def DividirListaTokens(lista_tokens):
#     indice = 0

#     while indice < len(lista_tokens):
#         if lista_tokens[indice].get_dato() == "=":
#             break
#         else:
#             indice += 1

#     lista_1 = lista_tokens[:indice]
#     lista_2 = lista_tokens[indice + 1:]
#     return lista_1, lista_2


