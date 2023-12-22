# adivinar un numero
import random

print("Bienvenido al juengo de adivinar un numero")
print('trata de adivinar un numero entre el 1 y el 10')

numero_secreto = random.randint(1, 10)
adivinado = False


while not adivinado:
    numero_usuario = int(input("ingresa un numero: "))
    if (numero_usuario == numero_secreto):
        print("felicidades has acertado")
        adivinado = True
    elif numero_usuario < numero_secreto:
        print("el numero secreto es mas alto")
    else:
        print('el numero secreto es mas bajo')
