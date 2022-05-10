import random
print ("JUEGO DEL AHORCADO")
print ("Presiona Enter para iniciar.")
inicio = input()

#Lista de palabras posibles
words = ["CALLE", "CARRO", "MUSEO", "PERRO", "VOLEIBOL", "ORO", "MARIHUANA", "COCA", "APARTAMENTO",
         "HUEVO", "JAGUAR", "BICICLETA", "FOTO", "FUEGO", "AGUA", "BOSQUE", "LAGUNA", "PLANETA", "MAGIA",
         "COMIDA", "HAMBURGUESA", "CODIGO", "ESTUDIAR", "PALABRAS", "FOTOGRAFIA", "CONCIERTO", "PARANORMAL",
         "WHISKY", "TEQUILA", "ROMANCE", "COMPUTADOR", "CIUDAD", "COLOMBIA", "ADVERTENCIA", "POKEMON", "PATINETA",
         "PATINES", "ZOOLOGICO", "MUSICA", "ANTROPOLOGIA", "INCLUSION", "SOCIABILIDAD", "MENUDENCIAS", "ARQUITECTURA",
         "TAMBORES", "IMPERIO", "COHERENCIA", "BOGOTA", "INDEPENDENCIA", "HUMANIDAD", "GALAXIA", "FRECUENCIA",
         "MAMBE", "ROSQUILLA", "QUESO", "PIZZA", "SUSHI", "AUDIFONOS"]

user = True

#Loop del juego
while user:
    
    #Elige palabra aleatoriamente
    word = random.choice(words)
    lifes = 6

    #Convierte string en lista con caracteres evaluables por separado y
    #crea listas vacías para la palabra del usuario y las letras que han sido jugadas
    game_word = list(word)
    user_word = []
    user_letters = []
    #print (game_word) para pruebas

    #Crea lista de "_ " según el largo de la palabra elegida
    for l in game_word:
        user_word.append("_")

    #Imprime la lista como caracteres separados por espacios    
    print ("\n", *user_word)

    game = True

    #Inicio de usuario a adivinar palabra
    while game:
        guess = False
        print ("\nEscribe una letra para adivinar la palabra. Tienes", lifes, "vidas.")
        user_letter = input()
        user_letter = user_letter.upper()

        #Validación de ingreso de letra
        if len(user_letter) != 1 or user_letter.isdigit():
            continue

        if user_letter in user_letters:
            print ("Ya usaste esa letra.")        
            continue

        user_letters.append(user_letter)

        #Comprobación de la letra de usuario en la palabra del juego a través de índice
        #porque función index() solo encuentra el primer caracter
        #Se reemplaza el "_", por la letra en caso de match
        for i in range(len(game_word)):
            if game_word[i] == user_letter:
                guess = True
                user_word[i] = user_letter.upper()

        print (*user_word)

        if not guess:
            lifes -= 1
            print ("La letra no está en la palabra.")
            
        if game_word == user_word:
            print ("Ganaste!")
            break
        if lifes <= 0:
            print ("Perdiste, tienes", lifes, "vidas.\nLa palabra era", word.upper()+".")
            break

    choice = input("\nPresiona enter para jugar de nuevo o X para salir:")
   
    if choice == "x":
        break