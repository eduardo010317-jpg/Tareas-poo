from mob import Mob

class Enderman(Mob):

    def hacer_sonido(self)  -> str:
        return "sonido distorsionado"
    
    def comportamiento(self)  -> str:
        return "neutral"
    
    def moverse(self)  -> str:
        return "se teletransporta"
    
    def reaccion_amirada(self, lo_miras:bool) -> str:
        if lo_miras:
            return "el enderman se enoja y ataca"
        else:
            return "el enderman esta tranquilo"