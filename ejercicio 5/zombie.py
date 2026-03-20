from mob import Mob

class Zombie(Mob):
    
    def hacer_sonido(self) -> str:
        return "grrrr"
    
    def comportamiento(self)  -> str:
        return "agresivo"
    
    def  moverse(self)  -> str:
        return "camina lentamente hacia el jugador"