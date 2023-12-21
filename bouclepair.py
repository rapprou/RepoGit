# Demande à l'utilisateur de saisir un nombre
limite = int(input("Entrez un nombre : "))
nombre = 1  # Initialise le nombre à 1

print(f"Les premiers nombres pairs jusqu'à {limite} sont :")

while nombre <= limite:
    # Vérifie si le nombre est pair en utilisant le modulo (%)
    if nombre % 2 == 0:
        print(nombre)
    nombre += 1  # Passe au nombre suivant

print("Fin du programme.")
###
