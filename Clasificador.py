from Token import Token
import re

class MiExcepcion(Exception):
    def __init__(self, mensaje):
        self.mensaje = mensaje

tipo_var={"int", "float", "double"}

caracteres_especiales = {
    "<Operador_Aritmetico>": ['+', '-', '/', '*', '^'],
    "<Operador_asignacion>": ['=', '+=', '-=', '=', '/=', '%=', '*=', '//='],
    "<Operador_Incremento>": ['++', '--'],
    "<Caracter_Agrupacion>": ['(', ')'],
}

def tokenizer(dato):
    tipo="No encontrado"
    regex = re.compile(r'^[a-zA-Z_]\w*$')
    regex_num = re.compile(r'^[+-]?\d+(\.\d+)?$')
    if (regex.match(dato)):
        tipo = "ID"
    elif(regex_num.match(dato)):
        tipo = "Numerico"
    else:
        raise MiExcepcion("Error!!!")
    nuevoToken = Token(dato, tipo)
    return nuevoToken

def es_caracter_esp(dato):
    encontrado=False
    for categoria,valor in caracteres_especiales.items():
        if dato in valor:
            encontrado = True
            break
    return encontrado

def tokenizer_caracter_esp(dato):
    tipo="No encontrado"
    for categoria,valor in caracteres_especiales.items():
        if dato in valor:
            tipo = categoria
            break
    if tipo == "No encontrado":
        raise MiExcepcion("Error!!!")
    nuevoToken = Token(dato, tipo)
    return nuevoToken
