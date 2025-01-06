#MENU OPERATION


#AFFICHER UN AUTOMATE
def affiche(matrice):
    print(matrice)
    return 0
#LIRE UN AUTOMATE
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


def miroir(automate):
    l=[]
    for i in range(len(automate)):
            l.append(automate[len(automate)-i-1])
    return l

def estComplet(automate):
    etat = len(automate)
    etat_cible = len(automate[0])
    for i in range (etat):
        for j in range(etat_cible):
            if(automate[i][j]==-1):
                return False
    return True

def rendreComplet(automate):
    if (estComplet(automate)=="True"):
        return automate
    else :
        new_etat = len(automate)
        etat_cible = len(automate[0])
        automate.append([new_etat]*len(automate[0]))
        for i in range (new_etat):
            for j in range(etat_cible):
                if(automate[i][j]==-1):
                    automate[i][j]=new_etat
    return automate

def concat(a,b):
    a.append(b)
    return a

def estdeterministe(tab):
    a = 0
    d1=len(tab)
    d2=len(tab[0])
    d3=len(tab[0][0])
    for i in range(d1):
        for j in range(d2):
            for k in range(d3):
                if(tab[i][j][k]==0):
                    a=a+1
            print(a)
            if(a>=2):
                return False
            a = 0
    return True

def menu_op():
    a = entre_automate()
    while True:
        try:
            x = int(input(
                "Bienvenu sur le menu Operation !\n"
                "Sélectionnez votre option :\n\n"
                "1. Afficher un automate\n"
                "2. Vérifier que l'automate est complet\n"
                "3. Rendre l'automate complet\n"
                "4. Concaténation de 2 automates\n"
                "5. Miroir d'un automate"
                "6. Vérifier que l'automate est complet\n"
                "7. Quitter\n\n"
            ))
            if 1 <= x <= 7:
                break
            else:
                print("Votre option ne fait pas partie des propositions ! Veuillez réessayer.")
        except ValueError:
            print("Entrée invalide. Veuillez entrer un nombre entre 1 et 5.")
    if (x == 1):
        print("Vous avez choisi : Afficher un automate.")
        affiche(a)
        menu_op()
    if (x == 2):
        print("Vous avez choisi : Vérifier que l'automate est complet")
        print(estComplet(a))
        menu_op()
    if (x == 3):
        print("Vous avez choisi : Rendre l'automate complet")
        print(rendreComplet(a))
        menu_op()
    if (x == 4):
        print("Vous avez choisi : Concaténation de 2 automates")
        print("Vous devez fournir un autre automate")
        b= entre_automate()
        print("Votre nouvel automate : ", concat(a,b))
        menu_op()
    if (x == 5):
        print("Vous avez choisi : Miroir d'un automate")
        print("Votre nouvel automate : ", miroir(a))
        menu_op()
    if (x == 6):
        print("Vous avez choisi : Vérifier que l'automate est complet")
        teb=entre_automate()
        print(estdeterministe(tab))
        menu_op()
    if (x == 7):
        print("Vous avez choisi : Quitter. Retour au menu principal !")
        menu_pricipal()
