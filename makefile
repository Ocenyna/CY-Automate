# Nom du fichier principal
MAIN=menu.py

# Fichiers sources
SOURCES=menu.py edition.py operation.py expression.py

# Interpréteur Python
PYTHON=python3

# Cible par défaut
all: run

# Cible pour exécuter le programme
run: $(SOURCES)
	$(PYTHON) $(MAIN)

# Cible pour vérifier les erreurs de syntaxe
check:
	$(PYTHON) -m py_compile $(SOURCES)

# Cible pour nettoyer les fichiers compilés
clean:
	rm -rf __pycache__

# Aide pour afficher les commandes disponibles
help:
	@echo "Commandes disponibles dans ce Makefile :"
	@echo "  make run     : Exécuter le fichier principal ($(MAIN))"
	@echo "  make check   : Vérifier les erreurs de syntaxe dans les fichiers Python"
	@echo "  make clean   : Supprimer les fichiers compilés (__pycache__)"
	@echo "  make help    : Afficher cette aide"
