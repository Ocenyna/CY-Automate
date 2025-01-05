# Makefile pour le projet Python

# Variables
PYTHON = python3
MAIN = menu.py
MODULES = edition.py operation.py expression.py

# Cibles
.PHONY: all run clean

# Cible par défaut
all: run

# Cible pour exécuter le programme principal
run:
	$(PYTHON) $(MAIN)

# Cible pour nettoyer les fichiers temporaires (si nécessaire)
clean:
	rm -f *.pyc __pycache__/*
