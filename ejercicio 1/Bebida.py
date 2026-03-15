from Platillo import Platillo

class Bebida(Platillo):
    def __init__(self, nombre ,Precio , temperatura):
        super() .__init__( nombre, Precio)
        self.temperatura= temperatura

    def tipo(self):
        print(f"Tipo: Bebida - {self.temperatura}")
        