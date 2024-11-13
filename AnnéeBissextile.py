# Fonction pour savoir si une année est bissextile ou non
def bissextile(annee):
    if annee % 4 == 0 and annee % 100 != 0 or annee % 400 == 0:
        return True
    return False


# Fonction d'affichage
def affichage(annee):
    if bissextile(annee):
        print(f"L'année {annee} est bissextile")
    else:
        print(f"L'année {annee} n'est pas bissextile")


# Menu
print("************************************************************************")
print("Pour tester si une année est bissextile, tapez 1.")
print("Pour connaitre toues les années bissextile entre deux dates, tapez 2.")
print("Pour quiter le programme, tapez 3.")
choix = int(input("Faites votre choix : "))

while choix != 3:

    if choix == 1:
        try:
            # On demande à l'utilisateur l'année qu'il souhaite tester
            annee = int(input("Entrez l'année à tester : "))
            affichage(annee)
        # On fait attention, si l'utilisateur fait une saisie invalide, le programme doit continuer
        except ValueError:
            print("Année invalide")

    elif choix == 2:
        # On demande les années "bornes" pour chercher les années bissextiles entre les deux
        print("Entrez les années bornes pour le test")
        annee_debut = int(input("Année de début : "))
        annee_fin = int(input("Année de fin : "))
        # On créer une liste qui va stocker toutes les années bissextiles comprises entre les deux bornes
        annees_bissextiles = []

        if annee_debut > annee_fin:
            print("L'année de début doit être la plus petite.")

        else :
            for i in range(annee_fin - annee_debut + 1):
                # On récupère toutes les années bissextile comprises entre les deux dates et on les stocke dans une liste
                if bissextile(annee_debut):
                    annees_bissextiles.append(annee_debut)
                annee_debut += 1

        # On affiche toutes les années bissextiles que l'on a récupéré
        for i in range(len(annees_bissextiles)):
            affichage(annees_bissextiles[i])

    else:
        # Si le choix n'est pas valide, on le signale à l'utilsateur
        print("Choix invalide.")

    # On réaffiche le menu
    print()
    print("************************************************************************")
    print("Pour tester si une année est bissextile, tapez 1.")
    print("Pour connaitre toues les années bissextile entre deux dates, tapez 2.")
    print("Pour quiter le programme, tapez 3.")
    choix = int(input("Faites votre choix : "))
