from  herramienta import Herramienta

class Espada(Herramienta):

    @property
    def nombre(self):
        return "Espada"
    
    def usar(self, objetivo: str) -> str:
        daño = self.calcular_daño()
        self.desgastar()
        return f"{self.nombre} de {self._material} ataca a {objetivo} (daño: {daño})"