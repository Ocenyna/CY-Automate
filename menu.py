from edition import menu_edition
from operation import menu_op
from expression import menu_expression

def menu_principal():
    while True:
        try:
            x = int(input(
                "Bienvenu sur le menu principal !\n"
                "Sélectionnez votre option :\n\n"
                "1. Edition\n"
                "2. Opération\n"
                "3. Analyse et Expression régulière\n"
                "4. Quitter\n\n"
            ))
            if 1 <= x <= 4:
                break
            else:
                print("Votre option ne fait pas partie des propositions ! Veuillez réessayer.")
        except ValueError:
            print("Entrée invalide. Veuillez entrer un nombre entre 1 et 5.")
    if (x == 1):
        print("Vous avez choisi : Edition.")
        menu_edition()
        menu_principal()
    if (x == 2):
        print("Vous avez choisi : Opération.")
        menu_op()
        menu_principal()
    if (x == 3):
        print("Vous avez choisi : Analyse et Expression régulière.")
        menu_expression()
        menu_principal()
    if (x == 4):
        print("Vous avez choisi : Quitter. Au revoir !")
        return 0
menu_principal()
