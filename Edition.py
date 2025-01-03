import numpy as np

#LIRE UNE MATRICE/AUTOMATE

def entrematrice():
    while True:
        try:
            # Demander à l'utilisateur d'entrer une matrice
            x = np.array(eval(input("Veuillez entrer votre matrice : \n\n")))
            # Si la saisie est valide, sortir de la boucle
            break
        except (ValueError, SyntaxError, NameError):
            print("Entrée invalide. Veuillez entrer une matrice valide.")
    return x

def entre_automate():
    while True:
        try:
            # Demander à l'utilisateur d'entrer un automate
            automate = eval(input("Veuillez entrer votre automate (par exemple : [[1, 2, 3], [4, 5, 6], [7, 8, 9]]) : \n\n"))

            # Vérifier si l'entrée est une liste de listes
            if not (isinstance(automate, list) and all(isinstance(row, list) for row in automate)):
                raise ValueError("L'automate doit être une liste de listes.")

            # Vérifier que tous les éléments internes sont valides (des nombre)
            for row in automate:
                if not all(isinstance(element, int) for element in row):
                    raise ValueError("Tous les éléments de l'automate doivent être des chaînes ou caractères.")

            # Si tout est correct, sortir de la boucle
            break
        except (SyntaxError, NameError):
            print("Entrée invalide. Utilisez des chaînes entre guillemets (par exemple : [[1, 2, 3], [4, 5, 6], [7, 8, 9]]).")
        except ValueError as ve:
            print(ve)

    return automate

#SAUVEGARDE DANS UN FICHIER

def sauvegarde(automate):
    try:
        # Ouvrir un fichier nommé 'matrice_python.txt' en mode écriture
        with open("matrice_python.txt", mode="w") as f:
            f.writelines(automate)
            print("Votre automate est sauvegardé dans le fichier 'matrice_python.txt'.")
        #Prevention des erreurs de permission
    except PermissionError:
        print("Erreur : Impossible d'écrire dans le fichier. Vérifiez les permissions.")
        #Prevention des erreurs inattendues
    except Exception as e:
        print(f"Une erreur inattendue est survenue : {e}")

#AFFICHE UN AUTOMATE

def affiche(matrice):
    print(matrice)
    return 0

#MENU PRINCIPAL EDITION


def menu_edition():
    while True:
        try:
            x = int(input(
                "Bienvenu sur le menu Edition !\n"
                "Sélectionnez votre option :\n\n"
                "1. Lire un automate depuis la console \n"
                "2. Afficher un automate\n"
                "3. Sauvegarde un automate\n"
                "4. Quitter\n\n"
            ))
            if 1 <= x <= 4:
                break
            else:
                print("Votre option ne fait pas partie des propositions ! Veuillez réessayer.")
        except ValueError:
            print("Entrée invalide. Veuillez entrer un nombre entre 1 et 5.")
    if (x == 1):
        print("Vous avez choisi : Lire un automate depuis la console")
        print("Voici votre automate : ", entre_automate())
        menu_edition()
    if (x == 2):
        print("Vous avez choisi : Afficher un automate.")
        affiche(entre_automate())
        menu_edition()
    if (x == 3):
        print("Vous avez choisi : Sauvegarde un automate")
        sauvegarde(entre_automate())
        menu_edition()
    if (x == 4):
        print("Vous avez choisi : Quitter. Retour au menu principal !")
        menu_pricipal()

