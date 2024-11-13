#Fonction pour savoir si une année est bissextile ou non
def bissextile(annee):
    if annee%4==0 and annee%100!=0 or annee%400==0:
        return True
    return False

#Fonction d'affichage
def affichage(annee):
    if bissextile(annee):
        print(f"L'année {annee} est bissextile")
    else:
        print(f"L'année {annee} n'est pas bissextile")

#Menu
print("************************************************************************")
print("Pour tester si une année est bissxtile, tapez 1.")
print("Pour connaitre toues les années bissextile entre deux dates, tapez 2.")
print("Pour quiter le programme, tapez 3.")
choix=int(input("Faites votre choix : "))

while choix!=3:
    annees_bissextiles = []

    if choix==1:
        annee=int(input("Entrez l'année à tester : "))
        affichage(annee)

    elif choix==2:
        print("Entrez les années bornes pour le teste")
        annee_debut = int(input("Année de début : "))
        annee_fin = int(input("Année de fin : "))

        for i in range(annee_fin-annee_debut+1):

            if bissextile(annee_debut):
                annees_bissextiles.append(annee_debut)
            annee_debut += 1

        print(annees_bissextiles)

    print("************************************************************************")
    print("Pour tester si une année est bissxtile, tapez 1.")
    print("Pour connaitre toues les années bissextile entre deux dates, tapez 2.")
    print("Pour quiter le programme, tapez 3.")
    choix = int(input("Faites votre choix : "))
