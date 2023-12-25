import random

# Génère un nombre aléatoire entre 1 et 100
# nombre_aleatoire = random.randint(1, 100)
# print(nombre_aleatoire)  # Affiche le nombre aléatoire généré

diviner_nombre = random.randint(1, 20)
print(diviner_nombre)
essais_restants = 5

print('Diviner un nombre entre 1 et 20 tu as 5 essaies')

while essais_restants > 0:
    essaie = int(input('essaie un nombre: '))
    if essaie < diviner_nombre:
        print('Trop petit')
    elif essaie > diviner_nombre:
        print('Trop grande')
    else:
        print(f'Bravo tu as diviner le nombre {diviner_nombre}')
        break  # sortir de la boucle

    essais_restants -= 1
    print(f'il te reste {essais_restants} essais')

if essais_restants == 0:
    print(f'Dommage le nombre à diviner etait {diviner_nombre}')
