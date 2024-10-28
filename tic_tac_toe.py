print()
print("Bienvenue sur le jeu!")
print()
print("BONNE CHANCE AUX JOUEURS")
print()
# une liste qui contient des chiffres de 0 à 8 pour afficher les numéros les cases de tableau  (pour facilité le choix )
tableau = [0, 1, 2, 3, 4, 5, 6, 7, 8]

# on crée une Fonction qui affiche le tableau numéroté
def print_tableau():
    print(f"{tableau[0]} | {tableau[1]} | {tableau[2]}")  # la première ligne (1)
    print("--|---|--")
    print(f"{tableau[3]} | {tableau[4]} | {tableau[5]}")  # la deuxième ligne (2)
    print("--|---|--")
    print(f"{tableau[6]} | {tableau[7]} | {tableau[8]}")  # la troisième ligne (3)

# on crée une Fonction pour vérifier si un joueur a gagné
def le_gagnant(liste):
    #on disigne une liste des possibilités pour gagner le jeu 
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # lignes
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # colonnes
        [0, 4, 8], [2, 4, 6]              # diagonales
    ]
    
    # Vérifie chaque condition de victoire
    return any(all(tableau[i] == liste  for i in condition) for condition in win_conditions)


joueur_1 = 'X'
joueur_2 = 'O'

# Lancer la partie de jeu
for tour in range(9):
    #afficher le tableau vide  numéroté 
    print_tableau()

    # Tour du joueur 1
    while True:
        #demander au joueur 1 de donner un chiffre pour placer le X
        move = input(f"Joueur 1 ({joueur_1}), choisissez un chiffre entre(0-8) pour placer le 'X': ")

        #on virifie si l'entrée donnée par le joueur 1 est bien un chiffre entre 0 et 9
        if move.isdigit() and 0 <= int(move) <= 8:

            #convirtir l'entrée donner par le jour en entier *
            move = int(move)
            #on virifie si la case demander par le joueur est vide (contient le numéro demander)
            if tableau[move] == move:
                #plcer X dans la case demander 
                tableau[move] = joueur_1
                break
            else:
                print("Cet emplacement est déjà pris, réessaye !")
        else:
            print("Option invalide, veuillez entrer un chiffre entre 0 et 8.")

    #on virifie si  le joueur 1 à gagner 
    if le_gagnant(joueur_1):
        #on affiche le tableau actuel(avec la dernière modification)
        print_tableau()
        print(f"Joueur 1 '{joueur_1}' a gagné !")
        print("Jeu terminé")
        break

    print_tableau()

    # Tour du joueur 2
    while True:
        move = input(f"Joueur 2 ({joueur_2}), choisissez un chiffre entre(0-8) pour placer le 'O': ")
        if move.isdigit() and 0 <= int(move) <= 8:
            move = int(move)
            if tableau[move] == move:
                tableau[move] = joueur_2
                break
            else:
                print("Cet emplacement est déjà pris, réessaye !")
        else:
            print("Option invalide, veuillez entrer un chiffre entre 0 et 8.")

    if le_gagnant(joueur_2):
        print_tableau()
        print(f"Joueur 2 '{joueur_2}' a gagné !")
        print("Jeu terminé")
        break

    if tour == 8:  # Si on a fait 9 tours sans gagnant
        print_tableau()
        print("Match nul !")
