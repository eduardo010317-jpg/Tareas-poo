from pico import Pico
from espada import Espada 
from pala import Pala

if __name__ == "__main__":

    herramientas= [
        Pico("diamante", 5),
        Espada("hierro", 3),
        Pala("madera", 2),
    ]

    objetivos = [" mena de diamante", "creeper", "arena"]

    for h, obj in zip(herramientas, objetivos):
        print(h.usar(obj))
        h.estado()
        print()