class Cliente: 
    
    #defino la clase Cliente con 4 atrib
    def __init__(self, nombre, apellido, email, clave):
        self.nombre =  nombre
        self.apellido = apellido
        self.email = email
        self.clave = clave

    def nombre_completo(self):
        return f"{self.nombre} {self.apellido}"

    def info_usario(self):
        return f"Email: {self.email}\nClave: {self.clave}"

    def __str__(self): 
        return f"Nombre: {self.nombre}\nApellido: {self.apellido}\nemail: {self.email}\nClave: {self.clave}"

