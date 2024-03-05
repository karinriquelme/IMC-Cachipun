import random
import sys

usuario=sys.argv[1]

opciones=["piedra", "papel", "tijeras"]
compu=random.choice(opciones)


if usuario in opciones:
    if usuario ==compu:
        print("Empate")
        print(f"tu jugaste {usuario}")
        print(f"computador jugo {compu}")
    elif ( (usuario=="piedra" and compu=="tijeras") or 
        (usuario=="papel"and compu=="piedra")  or 
        (usuario=="tijeras" and compu=="papel" )):
        print("Ganaste!!!")
        print(f"tu jugaste {usuario}")
        print(f"computador jugo {compu}")
    else:
        print("perdiste")
        print(f"tu jugaste {usuario}")
        print(f"computador jugo {compu}")
else:
    print("Argumento invalido, debe ser piedra, papel o tijeras")
