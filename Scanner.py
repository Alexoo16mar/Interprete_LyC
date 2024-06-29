import Clasificador as clas
from ConvertidorPosfija import conversionPosfija
from OperadorPosfija import evaluarExpresion
import Token
import AutomataPila as automata

class scanner():
    def __init__(self):
        self.lista_tokens=[]
        self.lista_simbolos={
            "sexo":69
        }

    def separador_tokens(self, linea):
        i=0
        self.lista_tokens.clear()
        palabra=""
        palabra_esp=""
        while i<len(linea):
            caracter = linea[i]
            if caracter == ' ':
                if palabra != '':
                    token = clas.tokenizer(palabra)
                    self.lista_tokens.append(token)
                palabra = ''
            elif clas.es_caracter_esp(caracter):
                if palabra != '':
                    token = clas.tokenizer(palabra)
                    self.lista_tokens.append(token)
                while i < len(linea) and clas.es_caracter_esp(linea[i]):
                    palabra_esp += linea[i]
                    i+=1
                token = clas.tokenizer_caracter_esp(palabra_esp)
                palabra_esp = ''
                self.lista_tokens.append(token)
                palabra = ''
            else:
                palabra += caracter
            i+=1
        if palabra != '':
            token = clas.tokenizer(palabra)
            self.lista_tokens.append(token)
    
    def DividirListaTokens(self):
        indice = 0
        while(indice<len(self.lista_tokens)):
            if(self.lista_tokens[indice].get_dato()=="="):
                break
            else:
                indice=indice+1
        lista_1=self.lista_tokens[:indice]
        lista_2=self.lista_tokens[indice+1:]
        return lista_1,lista_2
    
    def reconocer(self, string):
        self.separador_tokens(string)
        if automata.AutomataPilaEA(self.lista_tokens):
            if len(self.lista_tokens)>1:
                lista_1,lista_2=self.DividirListaTokens()
                if len(lista_1)==2:
                    lista_1[1].set_valor(evaluarExpresion(conversionPosfija(lista_2), self.lista_simbolos))
                    # agregamos un nuevo simbolo a la lista de simbolos
                    self.lista_simbolos[lista_1[1].get_dato()]=lista_1[1].get_valor()
                    print(lista_1[1].get_dato(), " = ",lista_1[1].get_valor())
                elif len(lista_1)==1:
                    lista_1[0].set_valor(evaluarExpresion(conversionPosfija(lista_2), self.lista_simbolos))
                    if lista_1[0].get_dato() not in self.lista_simbolos:
                        raise automata.MiExcepcion("La variable " + lista_1[0].get_dato() + " no ha sido declarada")
                    # alteramos el valor de un simbolo ya existente
                    self.lista_simbolos[lista_1[0].get_dato()]=lista_1[0].get_valor()
                    print(lista_1[0].get_dato(), " = ", lista_1[0].get_valor())
            else:
                if self.lista_tokens[0].get_dato() in self.lista_simbolos:
                    print(self.lista_tokens[0].get_dato(), " = ", self.lista_simbolos[self.lista_tokens[0].get_dato()])
                else:
                    raise automata.MiExcepcion("La variable " + self.lista_tokens[0].get_dato() + " no ha sido declarada")
        else:
            raise automata.MiExcepcion("Error! >> Expresion Incorrecta")
    
    def interprete(self):
        while True:
            try:
                expresion = input(">>")
                if expresion == "exit":
                    break
                self.reconocer(expresion)
            except automata.MiExcepcion as e:
                print(e.mensaje)
            print(self.lista_simbolos)

