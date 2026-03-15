from Comida import Comida
from Bebida import Bebida
from Postre import Postre

comida1 = Comida("Hamburguesa", 120.0, "Principal")
Bebida1 = Bebida("Limonada", 35.0, "Fria")
Postre1 = Postre("Pastel de Chocolate", 50.0, False)


comida1.mostrar_info()
comida1.tipo()

print("------------------------")

Bebida1.mostrar_info()
Bebida1.tipo()

print("------------------------")

Postre1.mostrar_info()
Postre1.tipo()