from vaca import Vaca
from creeper import Creeper
from enderman import Enderman
from zombie import Zombie   

if __name__ == "__main__":

    mobs = [
        Vaca("bessie", 10),
        Creeper("explosi",20),
        Enderman("tall boi",40),
        Zombie("walker", 15),
    ]
    
    for mob in mobs:
        mob.presentarse()


        if isinstance(mob, Enderman):
            print(" interaccion especial:")

            print(mob.reaccion_amirada(True))
            print()
