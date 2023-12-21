# print("Nom: " + nom)
# print('Prenom:' + prenom)
# print(f"Profession:, {profession}, {prenom}, {nom}")

######

# nom = input('Quel est ton nom ? ')
# age = input("Quel est votre age ? ")

# age = 30
# try:
#     age_prochain = int(age) + 1
# except:
#     print("ERROR: vous devez rentrer un nombre pour l'age")
# else:
#     print("Vous vous appellez: " + nom + " et vous avez " + str(age) + " ans")
#     print("L'an prochain vous aurez " + str(age_prochain) + " ans")


# print("ERROR: vous devez rentrer un nombre pour l'age")

########
# boucle

# n = 0  # cree la variable
# print(n)
# n = 1  # reafecte la variable
# print(n)
# n = n + 1  # incremente
# print(n)
# print('Debut de la boucle')
# while n < 10:
#     print('valeur de n; ' + str(n))
#     n = n + 1
# print('fin de la boucle')

# mot_de_passe = ""
# while not mot_de_passe == "TOTO":
#     mot_de_passe = input('quelest le mot de passe ?')
# print('mot de passe correct')

####
nom = input('Quel est votre nom ? ')


age = 0

while age == 0:
    age_str = input("Quel est votre age ? ")
    try:
        age = int(age_str) + 1
    except:
        print("ERROR: vous devez rentrer un nombre pour l'age")

print("Vous vous appellez: " + nom + " et vous avez " + str(age) + " ans")
print("L'an prochain vous aurez " + str(age + 1) + " ans")
