def menu_principal():
    while True:
        try:
            x = int(input(
                "Bienvenu sur le menu principal !\n"
                "Sélectionnez votre option :\n\n"
                "1. Edition\n"
                "2. Opération\n"
                "3. Analyse\n"
                "4. Expression régulière\n"
                "5. Quitter\n\n"
            ))
            if 1 <= x <= 5:
                break
            else:
                print("Votre option ne fait pas partie des propositions ! Veuillez réessayer.")
        except ValueError:
            print("Entrée invalide. Veuillez entrer un nombre entre 1 et 5.")
    if (x == 1):
        print("Vous avez choisi : Edition.")
        menu_edition()
    if (x == 2):
        print("Vous avez choisi : Opération.")
        menu_op()
    if (x == 3):
        print("Vous avez choisi : Analyse.")
        menu_expression()
    if (x == 4):
        print("Vous avez choisi : Expression régulière.")

    if (x == 5):
        print("Vous avez choisi : Quitter. Au revoir !")
        return 0
