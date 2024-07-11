class Token:
    def __init__(self, dato, tipo,id,tipo_var,valor):
        self.dato = dato
        self.tipo = tipo
        self.id=id
        self.tipo_var=tipo_var
        self.valor=valor
    
    def __init__(self, dato, tipo):
        self.dato = dato
        self.tipo = tipo
    
    def set_dato(self, nuevo_dato):
        self.dato = nuevo_dato
    
    def get_dato(self):
        return self.dato
    
    def set_tipo(self, nuevo_tipo):
        self.tipo = nuevo_tipo
    
    def get_tipo(self):
        return self.tipo
    
    def set_id(self, nuevo_id):
        self.id = nuevo_id
    
    def get_id(self):
        return self.id
    
    def set_tipo_var(self, nuevo_tipo_var):
        self.tipo_var = nuevo_tipo_var
    
    def get_tipo_var(self):
        return self.tipo_var
    
    def set_valor(self, nuevo_valor):
        self.valor = nuevo_valor
    
    def get_valor(self):
        return self.valor