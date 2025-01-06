import re
from menu import menu_principal

def verifier_expression_reguliere(expression, mot):
    try:
        motif = re.compile(expression)
        if motif.fullmatch(mot):
            print(f"Le mot '{mot}' est accepté par l'expression régulière '{expression}'.")
        else:
            print(f"Le mot '{mot}' n'est pas accepté par l'expression régulière '{expression}'.")
    except re.error as e:
        print(f"Erreur dans l'expression régulière : {e}")


def menu_expression():
    while True:
        try:
            # Demander à l'utilisateur une expression régulière
            expression = input(
                "Bienvenue sur le menu Expression régulière !\n"
                "Entrez une expression régulière : \n"
            )
            # Vérification de l'expression régulière
            try:
                re.compile(expression)  # Vérifie si l'expression est valide
            except re.error:
                print("L'expression régulière est invalide. Veuillez réessayer.")
                continue
            break
        except ValueError:
            print("Entrée invalide. Veuillez entrer une chaîne de caractères.")

    while True:
        try:
            # Demander un mot à tester
            mot = input("Entrez un mot à tester : \n")
            break
        except ValueError:
            print("Entrée invalide. Veuillez entrer une chaîne de caractères.")

    verifier_expression_reguliere(expression, mot)


    while True:
        try:
            x = int(input(
                "Bienvenu sur le menu Edition !\n"
                "Sélectionnez votre option :\n\n"
                "1. Entrez une expression régulière de nouveau \n"
                "2. Quitter\n"
            ))
            if 1 <= x <= 2:
                break
            else:
                print("Votre option ne fait pas partie des propositions ! Veuillez réessayer.")
        except ValueError:
            print("Entrée invalide. Veuillez entrer un nombre entre 1 et 6.")
    if (x == 1):
        print("Vous avez choisi : Entrez une expression régulière de nouveau")
        menu_expression()
    if (x == 2):
        print("Vous avez choisi : Quitter. Retour au menu principal !")
        menu_principal()
