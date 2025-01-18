
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

def modifier_automate(self, action, **kwargs):
        """
        Modifie l'automate selon une action spécifique.
        Actions possibles :
            - ajouter_etat
            - supprimer_etat
            - ajouter_transition
            - supprimer_transition
            - changer_etat_initial
            - ajouter_etat_final
            - supprimer_etat_final
        """
        if action == "ajouter_etat":
            self.etats.add(kwargs["etat"])

        elif action == "supprimer_etat":
            etat = kwargs["etat"]
            if etat in self.etats:
                self.etats.remove(etat)
                # Supprimer les transitions associées
                self.transitions = {
                    (src, sym): dests
                    for (src, sym), dests in self.transitions.items()
                    if src != etat and etat not in dests
                }
                # Supprimer des états finaux si nécessaire
                self.etats_finaux.discard(etat)

        elif action == "ajouter_transition":
            src, sym, dest = kwargs["source"], kwargs["symbole"], kwargs["destination"]
            if src in self.etats and dest in self.etats and sym in self.alphabet:
                if (src, sym) not in self.transitions:
                    self.transitions[(src, sym)] = set()
                self.transitions[(src, sym)].add(dest)

        elif action == "supprimer_transition":
            src, sym, dest = kwargs["source"], kwargs["symbole"], kwargs["destination"]
            if (src, sym) in self.transitions and dest in self.transitions[(src, sym)]:
                self.transitions[(src, sym)].remove(dest)
                if not self.transitions[(src, sym)]:
                    del self.transitions[(src, sym)]

        elif action == "changer_etat_initial":
            etat = kwargs["etat"]
            if etat in self.etats:
                self.etat_initial = etat

        elif action == "ajouter_etat_final":
            etat = kwargs["etat"]
            if etat in self.etats:
                self.etats_finaux.add(etat)

        elif action == "supprimer_etat_final":
            etat = kwargs["etat"]
            self.etats_finaux.discard(etat)

        else:
            raise ValueError("Action non reconnue : {}".format(action))

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
        return True
