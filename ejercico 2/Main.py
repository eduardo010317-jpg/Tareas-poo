from Guerrero import Guerrero
from Mago     import Mago
from Arquero  import Arquero


g =Guerrero("Kratos", 8, "Hacha")
m =Mago("Freya", 15, "Bola de fuego")
a =Arquero("Atreus", 10, 30)


g.presentarse()
g.usar_habilidad()

print("--------------")


m.presentarse()
m.usar_habilidad()

print("--------------")


a.presentarse()
a.usar_habilidad()