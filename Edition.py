import numpy as np
import os

#DEFINITION D'AUTOMATE

class Automate:
    def _init_(self, etats=None, alphabet=None, transitions=None, etat_initial=None, etats_finaux=None):
        self.etats = etats or set()
        self.alphabet = alphabet or set()
        self.transitions = transitions or {}
        self.etat_initial = etat_initial
        self.etats_finaux = etats_finaux or set()

    def _str_(self):
        representation = """Automate:
Etats: {etats}
Alphabet: {alphabet}
Transitions: {transitions}
Etat Initial: {etat_initial}
Etats Finaux: {etats_finaux}
""".format(
            etats=self.etats,
            alphabet=self.alphabet,
            transitions=self.transitions,
            etat_initial=self.etat_initial,
            etats_finaux=self.etats_finaux,
        )
        return representation


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
            matrice = eval(input("Veuillez entrer votre automate (par exemple : [[1, 2, 3], [4, 5, 6], [7, 8, 9]]) : \n\n"))

            # Vérifier si l'entrée est une liste de listes
            if not (isinstance(matrice, list) and all(isinstance(row, list) for row in matrice)):
                raise ValueError("L'automate doit être une liste de listes.")

            # Vérifier que tous les éléments internes sont valides (des nombre)
            for row in matrice:
                if not all(isinstance(element, int) for element in row):
                    raise ValueError("Tous les éléments de l'automate doivent être des nombres.")

            # Si tout est correct, sortir de la boucle
            break
        except (SyntaxError, NameError):
            print("Entrée invalide. Veuillez entrer un automate valide (par exemple : [[1, 2, 3], [4, 5, 6], [7, 8, 9]]).")
        except ValueError as ve:
            print(ve)

    return matrice

#SAUVEGARDE DANS UN FICHIER

def sauvegarde(matrice):
    try:
        # Ouvrir un fichier nommé 'matrice_python.txt' en mode écriture
        with open("matrice_python.txt", mode="w") as f:
            f.writelines(matrice)
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

#MODIFIER UN AUTOMATE

def modifier_automate(automate):
    while True :
        try :
            print("Modification de l'automate")
            print("1. Ajouter un état")
            print("2. Supprimer un état")
            print("3. Ajouter une transition")
            print("4. Supprimer une transition")
            print("5. Retour au menu principal")
            choix = int(input("Votre choix : "))

            if choix == "1":
                while True :
                    try :
                        etat = input("Entrez le nouvel état : ")
                        if not isinstance(etat, Automate):
                            raise TypeError("Il faut ecrire set([...])")
                        else:
                            break
                    except ValueError:
                        print("Il faut ecrire set([...])")
                automate.etats.add(etat)
                print(f"État {etat} ajouté.")
                return automate

            elif choix == "2":
                while True :
                    try :
                        etat = input("Entrez l'état à supprimer : ")
                        if not isinstance(etat, int):
                            raise TypeError("Il faut ecrire set([...])")
                        else:
                            break
                    except ValueError:
                        print("Il faut ecrire set([...])")
                automate.etats.discard(etat)
                automate.transitions = {
                    key: value
                    for key, value in automate.transitions.items()
                    if key[0] != etat and etat not in value
                }
                print(f"État {etat} supprimé.")
                return automate

            elif choix == "3":
                source = input("Entrez l'état source : ")
                symbole = input("Entrez le symbole : ")
                cible = input("Entrez l'état cible : ")
                if (source, symbole) not in automate.transitions:
                    automate.transitions[(source, symbole)] = set()
                automate.transitions[(source, symbole)].add(cible)
                print(f"Transition ({source}, {symbole}, {cible}) ajoutée.")
                return automate

            elif choix == "4":
                source = input("Entrez l'état source : ")
                symbole = input("Entrez le symbole : ")
                cible = input("Entrez l'état cible : ")
                if (source, symbole) in automate.transitions:
                    automate.transitions[(source, symbole)].discard(cible)
                    if not automate.transitions[(source, symbole)]:
                        del automate.transitions[(source, symbole)]
                    print(f"Transition ({source}, {symbole}, {cible}) supprimée.")
                    return automate

            elif choix == "5":
                return 0
            else:
                print("Choix invalide.")
        except ValueError:
                print("Choix invalide.")


#RECUPERER UN FICHIER


def rec():
    while True:
        try:
            # Demander à l'utilisateur le nom du fichier
            d = input("Quel est le nom du fichier ? Écrivez-le avec son extension, par exemple : matrice.txt\n")

            # Vérifier que le fichier existe
            if os.path.exists(d):
                print("Fichier trouvé.")
                return d
            else:
                print("Fichier introuvable. Veuillez entrer un fichier valide.")

        except Exception as e:

            print(f"Une erreur s'est produite : {e}. Veuillez réessayer.")


#CHARGER AUTOMATE

def charger_automate(fichier):
    try:
        with open(fichier, 'r') as f:
            lignes = f.readlines()
        etats = set(lignes[1].split(":")[1].strip().split())
        alphabet = set(lignes[2].split(":")[1].strip().split())
        transitions = {}
        lignes_transitions = lignes[3].split(":")[1].strip().split(',')
        for transition in lignes_transitions:
            if not transition.strip():
                continue
            source, symbole, cible = transition.strip('()').split()
            if (source, symbole) not in transitions:
                transitions[(source, symbole)] = set()
            transitions[(source, symbole)].add(cible)
        etat_initial = lignes[4].split(":")[1].strip()
        etats_finaux = set(lignes[5].split(":")[1].strip().split())
        return Automate(etats, alphabet, transitions, etat_initial, etats_finaux)
    except FileNotFoundError:
        print("Fichier non trouvé.")
        return None

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
                "4. Charger un automate depuis un fichier\n"
                "5. Modifier un automate\n"
                "6. Quitter\n\n"
            ))
            if 1 <= x <= 6:
                break
            else:
                print("Votre option ne fait pas partie des propositions ! Veuillez réessayer.")
        except ValueError:
            print("Entrée invalide. Veuillez entrer un nombre entre 1 et 6.")
    if (x == 1):
        print("Vous avez choisi : Lire un automate depuis la console")
        entre_automate()
        menu_edition()
    if (x == 2):
        print("Vous avez choisi : Afficher un automate.")
        a=entre_automate()
        affiche(a)
        menu_edition()
    if (x == 3):
        print("Vous avez choisi : Sauvegarde un automate")
        a=entre_automate()
        sauvegarde(a)
        menu_edition()
    if (x == 4):
        print("Vous avez choisi : Charger un automate")
        d = rec()
        charger_automate(fichier)
        menu_edition()
    if (x == 5):
        print("Vous avez choisi : Modifier un automate")
        m=entre_automate()
        n= modifier_automate(m)
        affiche(n)
        menu_edition()
    if (x == 6):
        print("Vous avez choisi : Quitter. Retour au menu principal !")
        menu_principal()

