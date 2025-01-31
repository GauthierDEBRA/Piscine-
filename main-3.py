liste = [("Pierre", "Dos", 10), ("Paul", "Brasse", 13), ("Léa", "Crawl", 6), ("Léa", "Brasse", 8)]
commande = ''

def afficher_menu():
    """Affiche le menu des options disponibles."""
    print("\n---- Gestionnaire de piscine ----")
    print("1 -> Ajouter une performance")
    print("2 -> Ajouter un individu (Non implémenté)")
    print("3 -> Ajouter une nouvelle nage (Non implémenté)")
    print("4 -> Lister toutes les performances")
    print("5 -> Lister les performances d'un nageur")
    print("6 -> Lister les nageurs pratiquant une nage")
    print("7 -> Sauvegarder les données")
    print("8 -> Charger les données")
    print("0 -> Quitter le logiciel")

def get_int_value(prompt):
    """Saisie sécurisée d'un entier"""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Veuillez entrer un nombre valide.")

def cmd_ajout(liste):
    """Ajoute un évènement à la liste"""
    a = input("Nom du nageur : ")
    b = input("Type de nage : ")
    c = get_int_value("Nombre de longueurs : ")
    liste.append((a, b, c))
    print("Performance ajoutée avec succès !")

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
    found = False
    for elt in liste:
        if elt[0] == tmp:
            print(f" {elt[1]:8}|  {elt[2]}")
            found = True
    if not found:
        print("Aucune performance trouvée pour ce nageur.")

def cmd_nage(liste):
    """Affiche toutes les performances suivant une nage donnée"""
    tmp = input("Type de nage : ")
    print(f"\nNage : {tmp}")
    print(" Nageur     |  Longueur")
    print("------------------------")
    found = False
    for elt in liste:
        if elt[1] == tmp:
            print(f" {elt[0]:11}|  {elt[2]}")
            found = True
    if not found:
        print("Aucun nageur trouvé pour cette nage.")

def cmd_exit(liste):
    """Demande confirmation avant de quitter"""
    tmp = input("En êtes-vous sûr ? (o)ui/(n)on ").lower()
    if tmp == 'o':
        cmd_save(liste, 'save.backup')
        print("Données sauvegardées. Au revoir !")
        return False
    return True

def cmd_save(liste, filename):
    """Sauvegarde la BDD"""
    with open(filename, 'w') as fichier:
        for elt in liste:
            fichier.write(f"{elt[0]},{elt[1]},{elt[2]}\n")
    print(f"Données sauvegardées dans {filename}.")

def cmd_load(liste, filename):
    """Charge la BDD"""
    try:
        with open(filename, 'r') as fichier:
            liste.clear()  # Pour éviter les doublons lors du rechargement
            for line in fichier:
                line = line.strip()
                if line and not line.startswith('#'):
                    tmp = line.split(',')
                    liste.append((tmp[0], tmp[1], int(tmp[2])))  # Convertir le nombre en entier
        print(f"Données chargées depuis {filename}.")
    except FileNotFoundError:
        print("Fichier introuvable. Veuillez sauvegarder d'abord.")

# Boucle principale avec le menu
isAlive = True
while isAlive:
    afficher_menu()  # Affiche le menu avant chaque saisie
    commande = get_int_value("\nVotre choix : ")  # Saisie sécurisée d'un entier

    if commande == 1:
        cmd_ajout(liste)
    elif commande == 2:
        print("Ajout d'un individu (à implémenter)")
    elif commande == 3:
        print("Ajout d'une nouvelle nage (à implémenter)")
    elif commande == 4:
        cmd_liste(liste)
    elif commande == 5:
        cmd_nageur(liste)
    elif commande == 6:
        cmd_nage(liste)
    elif commande == 7:
        cmd_save(liste, 'save.csv')
    elif commande == 8:
        cmd_load(liste, 'save.csv')
    elif commande == 0:
        isAlive = cmd_exit(liste)  # Quitter l'application
    else:
        print("Commande invalide. Veuillez choisir un numéro du menu.")
