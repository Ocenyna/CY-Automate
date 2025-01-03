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


def lire_automate_console():
    print("Saisie de l'automate :")
    etats = set(input("Entrez les états (séparés par des espaces) : ").split())
    alphabet = set(input("Entrez l'alphabet (séparé par des espaces) : ").split())
    transitions = {}
    print("Entrez les transitions sous la forme (état_source symbole état_cible), une par ligne. Tapez 'STOP' pour terminer.")
    while True:
        ligne = input("Transition : ")
        if ligne.strip().upper() == 'STOP':
            break
        source, symbole, cible = ligne.split()
        if (source, symbole) not in transitions:
            transitions[(source, symbole)] = set()
        transitions[(source, symbole)].add(cible)

    etat_initial = input("Entrez l'état initial : ")
    etats_finaux = set(input("Entrez les états finaux (séparés par des espaces) : ").split())

    return Automate(etats, alphabet, transitions, etat_initial, etats_finaux)


def afficher_automate(automate):
    print("\nAffichage de l'automate :")
    print(automate)


def sauvegarder_automate(automate, fichier):
    with open(fichier, 'w') as f:
        f.write(str(automate))
    print(f"Automate sauvegardé dans le fichier {fichier}")


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


def modifier_automate(automate):
    print("Modification de l'automate")
    print("1. Ajouter un état")
    print("2. Supprimer un état")
    print("3. Ajouter une transition")
    print("4. Supprimer une transition")
    print("5. Retour au menu principal")
    choix = input("Votre choix : ")

    if choix == "1":
        etat = input("Entrez le nouvel état : ")
        automate.etats.add(etat)
        print(f"État {etat} ajouté.")

    elif choix == "2":
        etat = input("Entrez l'état à supprimer : ")
        automate.etats.discard(etat)
        automate.transitions = {
            key: value
            for key, value in automate.transitions.items()
            if key[0] != etat and etat not in value
        }
        print(f"État {etat} supprimé.")

    elif choix == "3":
        source = input("Entrez l'état source : ")
        symbole = input("Entrez le symbole : ")
        cible = input("Entrez l'état cible : ")
        if (source, symbole) not in automate.transitions:
            automate.transitions[(source, symbole)] = set()
        automate.transitions[(source, symbole)].add(cible)
        print(f"Transition ({source}, {symbole}, {cible}) ajoutée.")

    elif choix == "4":
        source = input("Entrez l'état source : ")
        symbole = input("Entrez le symbole : ")
        cible = input("Entrez l'état cible : ")
        if (source, symbole) in automate.transitions:
            automate.transitions[(source, symbole)].discard(cible)
            if not automate.transitions[(source, symbole)]:
                del automate.transitions[(source, symbole)]
            print(f"Transition ({source}, {symbole}, {cible}) supprimée.")

    elif choix == "5":
        return
    else:
        print("Choix invalide.")


def menu_principal():
    automate = None
    while True:
        print("\nMenu Principal :")
        print("1. Edition")
        print("2. Operation (non implémenté dans cette version)")
        print("3. Analyse (non implémenté dans cette version)")
        print("4. Expression régulière (non implémenté dans cette version)")
        print("5. Quitter")
        choix = input("Votre choix : ")

        if choix == "1":
            print("\nMenu Edition :")
            print("1. Lire un automate à partir de la console")
            print("2. Afficher un automate")
            print("3. Sauvegarder un automate")
            print("4. Charger un automate depuis un fichier")
            print("5. Modifier un automate")
            print("6. Retour au menu principal")
            choix_edition = input("Votre choix : ")

            if choix_edition == "1":
                automate = lire_automate_console()
            elif choix_edition == "2":
                if automate:
                    afficher_automate(automate)
                else:
                    print("Aucun automate n'est chargé.")
            elif choix_edition == "3":
                if automate:
                    fichier = input("Entrez le nom du fichier : ")
                    sauvegarder_automate(automate, fichier)
                else:
                    print("Aucun automate à sauvegarder.")
            elif choix_edition == "4":
                fichier = input("Entrez le nom du fichier : ")
                automate = charger_automate(fichier)
                if automate:
                    print("Automate chargé avec succès.")
            elif choix_edition == "5":
                if automate:
                    modifier_automate(automate)
                else:
                    print("Aucun automate à modifier.")
            elif choix_edition == "6":
                continue
            else:
                print("Choix invalide.")

        elif choix == "5":
            print("Au revoir !")
            break
        else:
            print("Cette fonctionnalité n'est pas encore implémentée.")


if _name_ == "_main_":
    menu_principal()
