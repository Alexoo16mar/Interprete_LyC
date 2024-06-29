from Token import Token
import re
from AutomataPila import MiExcepcion


tipo_var={"entero", "real"}

caracteres_especiales = {
    "<Operador_Aritmetico>": ['+', '-', '/', '*', '^'],
    "<Operador_asignacion>": ['=', '+=', '-=', '=', '/=', '%=', '*=', '//='],
    "<Operador_Incremento>": ['++', '--'],
    "<Caracter_Agrupacion>": ['(', ')'],
}

def tokenizer(dato):
    tipo="No encontrado"
    if dato in tipo_var:
        tipo = "tipo_var"
        nuevoToken = Token(dato, tipo)
        return nuevoToken
    regex = re.compile(r'^[a-zA-Z_]\w*$')
    regex_num = re.compile(r'^[+-]?\d+(\.\d+)?$')
    if (regex.match(dato)):
        tipo = "ID"
        nuevoToken = Token(dato, tipo)
    elif(regex_num.match(dato)):
        tipo = "Numerico"
        nuevoToken = Token(dato, tipo)
        nuevoToken.set_valor(float(dato))
    else:
        raise MiExcepcion("Error!!!")
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
