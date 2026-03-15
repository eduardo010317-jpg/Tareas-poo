from    Platillo import Platillo

class Comida(Platillo):
    def  __init__(self, nombre, Precio, categoria):
        super().__init__(nombre, Precio)
        self.categoria = categoria

    def tipo(self):
        print(f"Tipo: Comida - {self. categoria}")