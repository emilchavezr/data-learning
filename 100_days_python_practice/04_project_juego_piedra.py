import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images = [rock, paper, scissors]

# Tu elección
print("Bienvenidos al juego de piedra, papel o tijera!")
usuario = int(input("Que quieres elegir? piedra(0) papel(1) o tijera(2) "))

if usuario >= 0 and usuario <= 2:
    print(game_images[usuario])

    computadora = random.randint(0, 2)
    print("La computador es: ")
    print(game_images[computadora])

    if computadora == 0 and usuario == 2:
        print("Perdiste!!!")
    elif usuario == 0 and usuario == 2:
        print("Ganaste!!")
    elif computadora > usuario:
        print("Perdiste!!")
    elif usuario > computadora:
        print("Ganaste!!")
    elif computadora == usuario:
        print("Empate!!!")
else:
    print("Opción invalida")
