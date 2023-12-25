import random

nombre_a_deviner = random.randint(1, 20)
essais_restants = 5

print("Devine un nombre entre 1 et 20. Tu as 5 essais.")

while essais_restants > 0:
    # input (ent) + variable
    essai = int(input("Essaie un nombre : "))

    if essai < nombre_a_deviner:
        print("Trop petit !")
    elif essai > nombre_a_deviner:
        print("Trop grand !")
    else:
        print(f"Bravo ! Tu as deviné le nombre {nombre_a_deviner} !")
        break  # Sort de la boucle si le nombre est deviné correctement

    essais_restants -= 1
    print(f"Il te reste {essais_restants} essais.")

if essais_restants == 0:
    print(f"Dommage ! Le nombre à deviner était {nombre_a_deviner}.")
