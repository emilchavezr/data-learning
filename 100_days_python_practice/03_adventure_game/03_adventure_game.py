print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

pregunta1 = input("Quieres ir a la izquierda de la isla, o a la derecha (Responder L o R) ").lower()

if pregunta1 == "l":
    print("Muy bien, vayamos al siguiente paso ")
    pregunta2 = input("Quieres nadar o esperar un barco que viene de camino? (Esperar o Barco) ").lower()
    if pregunta2 == "esperar":
        print("Muy bien, vayamos al siguiente paso ")
        pregunta3 = input("Que puerta quieres usar? La Azul, roja o amarilla? ")
        if pregunta3 != "amarilla":
            print("Acabas de caer al pantano, moriste!! ")
        else:
            print("GANASTEEEE!!!!!!!!! ")
    else:
        print("El barco estaba lleno de piratas, moriste ")
else:
    print("Comenzaste mal, ya te mató un cocodrilo ")
