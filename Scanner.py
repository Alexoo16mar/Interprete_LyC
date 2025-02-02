import Clasificador as clas
from ConvertidorPosfija import conversionPosfija
from OperadorPosfija import evaluarExpresion
import Token
import AutomataPila as automata

class scanner():
    def __init__(self):
        self.lista_tokens=[]
        self.lista_simbolos={
        }

    def separador_tokens(self, linea):
        i = 0
        self.lista_tokens.clear()
        linea.strip()
        palabra = ""
        palabra_esp = ""
        def add_token(string):
            if string != "":
                token = clas.tokenizer(string)
                self.lista_tokens.append(token)
        def add_caracter_esp_token(string):
            if string != "":
                token = clas.tokenizer_caracter_esp(string)
                self.lista_tokens.append(token)
        
        while i < len(linea):
            caracter = linea[i]
            if caracter == ' ':
                add_token(palabra)
                palabra = ''
            elif clas.es_caracter_esp(caracter):
                add_token(palabra)
                palabra = ''
                while i < len(linea) and clas.es_caracter_esp(linea[i]):
                    if not clas.es_caracter_esp(palabra_esp + linea[i]):
                        add_caracter_esp_token(palabra_esp)
                        add_caracter_esp_token(linea[i])
                        i += 1
                        palabra_esp = ''
                        continue
                    palabra_esp += linea[i]
                    i += 1
                add_caracter_esp_token(palabra_esp)
                palabra_esp = ''
                continue
            else:
                palabra += caracter
            i += 1
        add_token(palabra)
        if palabra_esp != '':
            add_caracter_esp_token(palabra_esp)
    
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
        if self.lista_tokens[0].get_dato() == "cout":
            if not self.lista_tokens[1].get_dato() == "<<":
                raise automata.MiExcepcion("Error! >> Expresion Incorrecta")
            if self.lista_tokens[2].get_tipo() == "ID":
                if self.lista_tokens[2].get_dato() not in self.lista_simbolos:
                    raise automata.MiExcepcion("La variable " + self.lista_tokens[2].get_dato() + " no ha sido declarada")
                print(self.lista_simbolos[self.lista_tokens[2].get_dato()])
            return
        
        if not automata.AutomataPilaEA(self.lista_tokens):
            raise automata.MiExcepcion("Error! >> Expresion Incorrecta")
        else:
            lista_1, lista_2 = self.DividirListaTokens()
            lista_1[0].set_valor(evaluarExpresion(conversionPosfija(lista_2), self.lista_simbolos))
            self.lista_simbolos[lista_1[0].get_dato()] = lista_1[0].get_valor()
    
    def interprete(self):
        while True:
            try:
                expresion = input(">>")
                if expresion == "exit":
                    break
                elif expresion == "clear":
                    self.lista_simbolos.clear()
                    continue
                elif expresion == "tabla":
                    print(self.lista_simbolos)
                    continue
                self.reconocer(expresion)
            except automata.MiExcepcion as e:
                print(e.mensaje)
            # Para atrapar una division entre cero:
            except ZeroDivisionError:
                print("Error! >> Division entre cero")
            except Exception as e:
                print("Error! >> Expresion Incorrecta")
            #print(self.lista_simbolos)

