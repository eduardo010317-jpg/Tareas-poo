from herramienta import Herramienta

class Pala(Herramienta):

    @property
    def nombre(self):
        return "Pala"
          
    def usar(self, objetivo: str) -> str:
        daño = self.calcular_daño()
        self.desgastar()
        return f"{self.nombre} de {self._material} excava {objetivo} (daño: {daño})"