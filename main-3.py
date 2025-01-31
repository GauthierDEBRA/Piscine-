liste = [("Pierre", "Dos", 10), ("Paul", "Brasse", 13), ("Léa", "Crawl", 6), ("Léa", "Brasse", 8)]

def afficher_menu():
    """Affiche le menu des options disponibles."""
    print("\n---- Menu ----")
    print("1 -> Ajouter une performance")
    print("2 -> Ajouter un individu")
    print("3 -> Ajouter une nouvelle nage")
    print("4 -> Lister toutes les performances")
    print("5 -> Lister les performances d'un nageur")
    print("6 -> Lister tous les nageurs pratiquant une nage")
    print("7 -> Sauvegarder les données")
    print("8 -> Charger les données")
    print("0 -> Quitter le logiciel")

def cmd_ajout(liste):
    """Ajoute un évènement à la liste"""
    a = input("Nom du nageur : ")
    b = input("Type de nage : ")
    c = input("Nombre de longueurs : ")
    liste.append((a, b, c))

def cmd_liste(liste):
    """Affiche toutes les performances des nageurs"""
    print("\nPrénom      |  Nage    |  Longueur")
    print("---------------------------------")
    for elt in liste:
        print(f" {elt[0]:11}| {elt[1]:8}|  {elt[2]}")

def cmd_nageur(liste):
    """Affiche toutes les performances d'un nageur"""
    tmp = input("Nom du nageur : ")
    print(f"\nPerformances de {tmp}")
    print("  Nage   |  Longueur")
    print("--------------------")
    for elt in liste:
        if elt[0] == tmp:
            print(f" {elt[1]:8}|  {elt[2]}")

def cmd_nage(liste):
    """Affiche toutes les performances suivant une nage donnée"""
    tmp = input("Type de nage : ")
    print(f"\nNage : {tmp}")
    print(" Nageur     |  Longueur")
    print("------------------------")
    for elt in liste:
        if elt[1] == tmp:
            print(f" {elt[0]:11}|  {elt[2]}")

def cmd_exit():
    """Quitte le programme"""
    print("Au revoir !")
    return False

isAlive = True
while isAlive:
    afficher_menu()  # Affiche le menu avant chaque saisie
    commande = input("Votre choix : ")  # Saisie de la commande

    if commande == "1":
        cmd_ajout(liste)
    elif commande == "2":
        print("Ajout d'un individu (Non implémenté)")
    elif commande == "3":
        print("Ajout d'une nouvelle nage (Non implémenté)")
    elif commande == "4":
        cmd_liste(liste)
    elif commande == "5":
        cmd_nageur(liste)
    elif commande == "6":
        cmd_nage(liste)
    elif commande == "7":
        print("Sauvegarde des données (Non implémenté)")
    elif commande == "8":
        print("Chargement des données (Non implémenté)")
    elif commande == "0":
        isAlive = cmd_exit()  # Quitter l'application
    else:
        print("Commande invalide. Veuillez choisir un numéro du menu.")
