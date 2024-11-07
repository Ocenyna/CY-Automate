# CY-Automate

Ce projet est un éditeur textuel pour manipuler et analyser des automates finis. Il permet la création, l'importation, la modification et la sauvegarde d'automates, ainsi que la réalisation de diverses opérations sur ceux-ci. L'éditeur est conçu pour offrir une interface textuelle conviviale permettant de travailler avec des automates sous forme de dictionnaire ou de matrice.

## Fonctionnalités

### Menu Principal

1. **Manipulation des automates** :
   - **Saisie d'un automate** : Permet à l'utilisateur de créer un nouvel automate en saisissant les états, les symboles et les transitions.
   - **Importer un automate** : Charge un automate depuis un fichier.
   - **Modifier un automate** : Ajoute ou modifie des transitions ou des états existants.
   - **Sauvegarder un automate** : Enregistre un automate dans un fichier pour une utilisation ultérieure.
   - **Afficher un automate** : Affiche les états, les symboles et les transitions d'un automate.
   - **Supprimer un automate** : Permet de supprimer un automate en mémoire.
   - **Afficher la matrice d'un automate** : Affiche l'automate sous forme de matrice d'adjacence.
   - **Retour au menu principal** : Permet de revenir au menu principal depuis le sous-menu de manipulation.

2. **Opérations sur les automates** :
   - **Est déterministe ?** : Vérifie si l'automate est déterministe.
   - **Est complet ?** : Vérifie si l'automate est complet.
   - **Rendre déterministe** : Convertit un automate en un automate déterministe.
   - **Rendre complet** : Ajoute les transitions manquantes pour rendre l'automate complet.
   - **Cloner un automate** : Crée une nouvelle copie de l'automate en mémoire.
   - **Calculer le complément** : Calcule le complément d'un automate (nécessite un automate complet).
   - **Miroir d'un automate** : Inverse les transitions de l'automate.
   - **Concaténation de deux automates** : Concatène deux automates pour former un nouvel automate.
   - **Produit de deux automates** : Effectue le produit cartésien de deux automates.
   - **Nettoyer un automate** : Supprime les états inaccessibles.

3. **Langage et expression régulière** :
   - (À définir selon les spécifications du projet ou les fonctionnalités souhaitées)

## Structure de données

Les automates peuvent être représentés sous forme de dictionnaire ou de matrice. Dans la représentation en dictionnaire, chaque état est associé à une liste de tuples représentant les transitions. Une matrice peut être utilisée pour visualiser les connexions entre états de manière plus compacte.


## Installation

1. Clonez ce dépôt ou téléchargez le code source.
2. Assurez-vous d'avoir Python installé (version 3.x recommandée).
3. Exécutez le fichier principal pour démarrer l'éditeur textuel.

```bash
python editeur_automate.py
```

## Guide d'utilisation

1. **Démarrage** : Après avoir lancé le programme, choisissez parmi les options du menu pour manipuler ou effectuer des opérations sur les automates.
2. **Manipulation d'automates** : Sélectionnez les options pour créer, modifier ou afficher un automate.
3. **Opérations sur les automates** : Accédez aux fonctionnalités avancées pour vérifier, transformer ou calculer des propriétés d'automates. (NON DISPONIBLES POUR L'INSTANT)
4. **Langage et expression régulière** : Utilisez les outils pour travailler avec des expressions régulières (NON DISPONIBLES POUR L'INSTANT)


## Améliorations futures

- Support des expressions régulières.

Ce README couvre les fonctionnalités principales de l'éditeur d'automates. N'hésitez pas à l'adapter pour refléter les nouvelles fonctionnalités au fur et à mesure de l'évolution du projet.

## Fichiers

- `editeur_automate.py` : fichier principal pour exécuter le programme.
- `README.md` : ce fichier, contenant la documentation du projet.

## Licence

Ce projet est sous licence GENERAL PUBLIC LICENSE. Vous êtes libre de l'utiliser, le modifier et le distribuer.
