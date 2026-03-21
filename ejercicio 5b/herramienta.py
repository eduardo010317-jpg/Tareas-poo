from abc import ABC, abstractmethod

DAÑO_MATERIAL = {
    "madera"    : 2,
    "piedra"    : 3,
    "hierro"    : 4,
    "oro"       : 3,  
    "diamante"  : 6,
    "netherita" : 8,
}


class Herramienta(ABC):

    def __init__(self, material: str, durabilidad: int):
        self._material      = material.lower()
        self._durabilidad    = durabilidad
        self._usos_restantes = durabilidad

    @property
    @abstractmethod
    def nombre(self) -> str:
        pass

    @abstractmethod
    def usar(self, objetivo: str) -> str:
        pass

    def calcular_daño(self) -> int:
        return DAÑO_MATERIAL.get(self._material, 1)

    def desgastar(self):
        if self._usos_restantes > 0:
            self._usos_restantes -= 1

    @property
    def rota(self) -> bool:
        return self._usos_restantes == 0

    def estado(self):
        txt = "💔 ROTA" if self.rota else f"✅ {self._usos_restantes} usos"
        print(f"[{self.nombre} de {self._material}] {txt}")