from perro import Perro
from bobino import Bobino
class Granja:
    def __init__ (self):
        self.miperro=[]
        self.mibovino=[]
        

    def agregar_perro(self, peso, edad, raza, propietario, fecha_vacunacion ):

        if len(self.miperro)==0:        
            perro=Perro()
            perro.edad=edad()
            perro.peso=peso()
            perro.raza=raza()
            perro.propietario=propietario()
            perro.fecha_vacuncion=fecha_vacunacion()
            self.miperro.append(perro)
        else:
            pass

    def agregar_bovino(self, peso, edad, raza, propietario, fecha_vacunacion):
        if len(self.mibovino)==0:        
            bovino=Bobino()
            bovino.edad=edad()
            bovino.peso=peso()
            bovino.raza=raza()
            bovino.propietario=propietario()
            bovino.fecha_vacuncion=fecha_vacunacion()
            self.mibovino.append(bovino)
        else:
            pass

    def obtener_perro(self):
        self.miperro
    
    def obtener_bovino(self):
        self.mibovino