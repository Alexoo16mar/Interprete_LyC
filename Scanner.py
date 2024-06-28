import Clasificador as clas
import Token

class scanner():
    def __init__(self):
        self.lista_tokens=[]

    def separador_tokens(self, linea):
        i=0
        while i<len(linea):
            caracter = linea[i]
            palabra=""
            palabra_esp=""
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
    
    def reconocer(self, string):
        self.separador_tokens(string)
        
    
    def interprete(self):
        while true:
            print("Ingrese una expresion")
            expresion = input()
            if expresion == "exit":
                break
            self.reconocer(expresion)
            