# tableau morpion
print("\n\nBienvenue sur le jeu!\n")
print("\n\nBONNE CHANCE AUX JOUEURS\n")

print()

tableau= [' ' for i in range(9)] # une liste pour contenir le tableau

def print_tableau():
    print(f"{tableau[0]} | {tableau[1]} | {tableau[2]}") # la première ligne (1)
    print("--|---|--")
    print(f"{tableau[3]} | {tableau[4]} | {tableau[5]}") # la deuxième ligne (2)
    print("--|---|--")
    print(f"{tableau[6]} | {tableau[7]} | {tableau[8]}") # la troisième ligne (3)


def le_gagnant(player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], #lignes
        [0, 3, 6], [1, 4, 7], [2, 5, 8], # colonne              # toutes les possibilités pour faire comprendre qu'un joueur a gagné 
        [0, 4, 8], [2, 4, 6]             # diagonal
    ]
    return any((tableau[1] == player for i in condition) for condition in win_conditions)
    
joueur_actuel = 'X'
for tour in range(9):
    print_tableau()
    while True:
        print()
        move = input(f"Joueur {joueur_actuel}, écrit un chiffre pour placer ton symbole entre (1-9):")
        if move.isdigit() and 1 <= int(move) <= 9:
            move = int(move) 
            if tableau[move] == " ":
                tableau[move] = joueur_actuel
                break

            else:
                print("cet emplacement est déjà pris, réessaye !")
        else:
            print("option invalid veuillez entrer un chiffre entre 1 et 9,")


            if le_gagnant(joueur_actuel):
                print_tableau()
                print()
                print(f"Joueur{joueur_actuel} a gagné !")
                break                                      # boucle cassé si un joueur gagne
            
            
            joueur_actuel = '0' if joueur_actuel == 'X' else 'X'
else:
    print_tableau()
print()
print("égalité")














