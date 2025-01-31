from datetime import datetime

# Fonction pour récupérer une valeur entière en toute sécurité
def get_int_value(prompt="Valeur ? "):
    """Saisie sécurisée d'un entier (évite les erreurs de format)"""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Indiquez bien une valeur numérique.")

def get_date_value(prompt="Date (YYYY-MM-DD) : "):
    """Saisie sécurisée d'une date au format YYYY-MM-DD"""
    while True:
        date_str = input(prompt)
        try:
            datetime.strptime(date_str, "%Y-%m-%d")  # Vérifie si la date est valide
            return date_str
        except ValueError:
            print("Format invalide. Entrez la date au format YYYY-MM-DD.")

liste = [
    ("Pierre", "Dos", 10, "2024-05-10"),
    ("Paul", "Brasse", 13, "2024-05-12"),
    ("Léa", "Crawl", 6, "2024-05-11"),
    ("Léa", "Brasse", 8, "2024-05-13")
]

def afficher_menu():
    """Affiche le menu des options disponibles."""
    print("\n---- Gestionnaire de piscine ----")
    print("1 -> Ajouter une performance")
    print("2 -> Ajouter un individu (Non implémenté)")
    print("3 -> Ajouter une nouvelle nage (Non implémenté)")
    print("4 -> Lister toutes les performances")
    print("5 -> Lister les performances d'un nageur (avec statistiques)")
    print("6 -> Lister les nageurs pratiquant une nage")
    print("7 -> Sauvegarder les données")
    print("8 -> Charger les données")
    print("9 -> Lister les performances d'un jour")
    print("0 -> Quitter le logiciel")

def cmd_ajout(liste):
    """Ajoute un évènement à la liste"""
    a = input("Nom du nageur : ")
    b = input("Type de nage : ")
    c = get_int_value("Nombre de longueurs : ")
    d = get_date_value("Date (YYYY-MM-DD) : ")
    liste.append((a, b, c, d))
    print("Performance ajoutée avec succès !")

def cmd_liste(liste):
    """Affiche toutes les performances des nageurs"""
    print("\nPrénom      |  Nage    |  Longueur |  Date")
    print("---------------------------------------------")
    for elt in liste:
        print(f" {elt[0]:11}| {elt[1]:8}|  {elt[2]:8} | {elt[3]}")

def cmd_nageur(liste):
    """Affiche toutes les performances d'un nageur avec statistiques"""
    tmp = input("Nom du nageur : ")
    performances = [elt for elt in liste if elt[0] == tmp]

    if not performances:
        print("Aucune performance trouvée pour ce nageur.")
        return

    print(f"\nPerformances de {tmp}")
    print("  Nage   |  Longueur")
    print("----------------------")
    
    longueurs = []
    for elt in performances:
        print(f" {elt[1]:8}|  {elt[2]:8}")
        longueurs.append(elt[2])

    # Calcul des statistiques
    min_perf = min(longueurs)
    max_perf = max(longueurs)
    moyenne = sum(longueurs) / len(longueurs)

    print("\nStatistiques :")
    print(f"Minimum  : {min_perf}")
    print(f"Maximum  : {max_perf}")
    print(f"Moyenne  : {moyenne:.1f}")

def cmd_nage(liste):
    """Affiche toutes les performances suivant une nage donnée"""
    tmp = input("Type de nage : ")
    print(f"\nNage : {tmp}")
    print(" Nageur     |  Longueur |  Date")
    print("----------------------------------")
    found = False
    for elt in liste:
        if elt[1] == tmp:
            print(f" {elt[0]:11}| {elt[2]:8} | {elt[3]}")
            found = True
    if not found:
        print("Aucun nageur trouvé pour cette nage.")

def cmd_par_jour(liste):
    """Affiche toutes les performances d'une date donnée"""
    date_recherche = get_date_value("Entrez une date (YYYY-MM-DD) : ")
    print(f"\nPerformances du {date_recherche}")
    print(" Nageur     |  Nage    |  Longueur")
    print("--------------------------------------")
    found = False
    for elt in liste:
        if elt[3] == date_recherche:
            print(f" {elt[0]:11}| {elt[1]:8}|  {elt[2]:8}")
            found = True
    if not found:
        print("Aucune performance enregistrée ce jour-là.")

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
            fichier.write(f"{elt[0]},{elt[1]},{elt[2]},{elt[3]}\n")
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
                    liste.append((tmp[0], tmp[1], int(tmp[2]), tmp[3]))  # Convertir le nombre en entier
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
        cmd_nageur(liste)  # Maintenant avec statistiques !
    elif commande == 6:
        cmd_nage(liste)
    elif commande == 7:
        cmd_save(liste, 'save.csv')
    elif commande == 8:
        cmd_load(liste, 'save.csv')
    elif commande == 9:
        cmd_par_jour(liste)
    elif commande == 0:
        isAlive = cmd_exit(liste)  # Quitter l'application
    else:
        print("Commande invalide. Veuillez choisir un numéro du menu.")
