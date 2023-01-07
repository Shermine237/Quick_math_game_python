import random

NOMBRE_MIN = 1
NOMBRE_MAX = 10
NOMBRE_DE_QUESTION = 4


def menu():
    selection = 0
    print("MENU")
    print("1- Addition")
    print("2- Soustration")
    print("3- Multiplication")
    print("4- Divisiom")
    print("5- Hasard")
    print("6- Quitter")
    while selection not in range(1, 7):
        try:
            selection = int(input("Choisissez un operateur :    "))
        except:
            print("Mauvaise saisie, veuillez ressayer")
    if selection == 5:
        return random.randint(1, 4)
    return selection


def demande_utilisateur():
    reponse = 0
    while reponse == 0:
        try:
            reponse = int(input("Quelle est la reponse de ce calcul ?     "))
        except:
            print("Mauvaise saisie, veuillez ressayer")
    return reponse


def verification(resultat, nb_question):
    reponse_saisie = demande_utilisateur()
    if reponse_saisie == resultat:
        print("Bonne reponse !")
        nb_question -= 1
        if nb_question == 0:
            print(f"Bravo vous avez trouve {NOMBRE_DE_QUESTION} questions")
    else:
        print("Mauvaise reponse !")
    print(f"Il vous reste {nb_question} questions")
    return nb_question


def addition():
    nb1 = random.randint(NOMBRE_MIN, NOMBRE_MAX)
    nb2 = random.randint(NOMBRE_MIN, NOMBRE_MAX)
    print(f"{nb1} + {nb2} = ?")
    return nb1+nb2


def soustration():
    nb1 = random.randint(NOMBRE_MIN, NOMBRE_MAX)
    nb2 = random.randint(NOMBRE_MIN, NOMBRE_MAX)
    print(f"{nb1} - {nb2} = ?")
    return nb1 - nb2


def multiplication():
    nb1 = random.randint(NOMBRE_MIN, NOMBRE_MAX)
    nb2 = random.randint(NOMBRE_MIN, NOMBRE_MAX)
    print(f"{nb1} * {nb2} = ?")
    return nb1 * nb2


def division():
    nb1 = random.randint(NOMBRE_MIN, NOMBRE_MAX)
    nb2 = random.randint(NOMBRE_MIN, NOMBRE_MAX)
    print(f"{nb1} / {nb2} = ?")
    return nb1 / nb2


print("     JEU DE MATHS")
nb_question_restantes = NOMBRE_DE_QUESTION

while not nb_question_restantes == 0:
    selectionMenu = menu()
    if selectionMenu == 1:
        nb_question_restantes = verification(addition(), nb_question_restantes)
    elif selectionMenu == 2:
        nb_question_restantes = verification(soustration(), nb_question_restantes)
    elif selectionMenu == 3:
        nb_question_restantes = verification(multiplication(), nb_question_restantes)
    elif selectionMenu == 4:
        nb_question_restantes = verification(division(), nb_question_restantes)
    elif selectionMenu == 6:
        print(" Bye Bye")
        break
