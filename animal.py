
class Animal:
    def __init__ (self):
       self.peso=""
       self.edad=""
       self.raza=""
    def Correr(self):
        if self.edad>=5:
            print("rapido")
        elif self.edad<5:
            print("lento")

    def emitir_sonido(self):
        pass

    def obtener_edad(self):
        pass
