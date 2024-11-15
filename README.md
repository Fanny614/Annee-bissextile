# Année bissextile
Ce script python permet de savoir si une année est bissextile ou non, ou d'avoir toute les années bissextiles comprise entre deux dates.

## Installation
Pour executer le script, il faut [python](https://www.python.org/downloads/).

### Installation de poetry
Pour plus d'information sur [poetry](https://python-poetry.org/).
```bash
curl -sSL https://install.python-poetry.org | python3 -
```

### Initialisation de poetry
```bash
poetry init
```
Pour créer et activer l'environnement virtuel avec poetry
```bash
poetry shell
```

### Package à installer
Pour l'afichage, il faut installer le package typer.
```bash
poetry add typer
```

## Usage
Pour exécuter le script dans le terminal :
```bash
python AnneeBissextile.py
```
ou 
```bash
typer AnneeBissextile.py run
```
Sinon il suffit de run le scrit.
