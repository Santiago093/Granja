from animal import Animal
class Bobino:
    def __init__ (self):

        self.propietario=""
        self.Fecha_vacunacion=""
        self.establo=5

    def pastor(self):

        if self.establo>5:
            print("pastar")

        else:
            print("No pastar")


    def emitir_sonido2(self):
        print("Muuu")