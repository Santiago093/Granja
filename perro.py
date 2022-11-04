from animal import Animal
class Perro:
    def __init__ (self):
        self.propietario=""
        self.fecha_vacuncion=""
        self.animal=Animal()

    def emitir_sonido(self):
        if self.edad<=3:
            print("auf auf")

        if self.edad>3:
            print("Guau Guau")

    

        