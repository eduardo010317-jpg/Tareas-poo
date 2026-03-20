from mob import Mob

class Creeper(Mob):
    
    def hacer_sonido(self)  -> str:
        return "...ssssss"
    
    def  comportamiento(self)  -> str:
        return "agresivo"
    
    def moverse(self)  -> str:
        return "corre directamente hacia el jugador"