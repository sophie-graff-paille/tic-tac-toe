import random

# tableau vide pour commencer le jeu
def Jeu():
    board = [' ', ' ', ' ',
             ' ', ' ', ' ',
             ' ', ' ', ' ']
    return board

# afficher le tableau dans le terminal
def displayBoard(board):
    print(board[0], ' |', board[1], '|', board[2])
    print('---+---+---')
    print(board[3], ' |', board[4], '|', board[5])
    print('---+---+---')
    print(board[6], ' |', board[7], '|', board[8])

# le joueur choisit la lettre qu'il veut être
def choixlettre():
    lettre = ""
    while not(lettre == "X" or lettre == "O"):
        print("Quelle lettre voulez-vous : X ou O ?")
        lettre = input().upper()
    if lettre == "X":
       return["X", "O"]
    else:
        return["O", "X"]

# fonction qui annonce quel joueur (X ou O) doit jouer,
# quel choix de case entre 1 et 9, si elle n'est pas déjà remplie,
# et qui retourne le tableau avec le tour joué
def play(player, board):
    print("\nC'est au joueur", player, "de jouer")
    answer = int(input('Quelle case voulez-vous cocher ? : '))
    while (answer <= 0 or answer >= 10 or board[answer - 1] != ' '):
        print("La case est invalide !")
        answer = int(input('Quelle case voulez-vous cocher ? : '))
    board[answer - 1] = player
    return board

# fonction qui affiche un message et qui retourne "True" si un joueur a gagné,
# sinon la fonction retourne "False"
# avec une liste des combos gagnants pour les parcourir avec un for pour éviter trop de if
combosgagnants = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

def gagnant(board):
    global combosgagnants
    for i in range(0, len(combosgagnants)):
        if (board[combosgagnants[i][0]] == board[combosgagnants[i][1]] and board[combosgagnants[i][1]] == board[combosgagnants[i][2]] and
                board[combosgagnants[i][0]] != ' '):
            displayBoard(board)
            print('\nLe joueur', board[combosgagnants[i][0]], 'gagne la partie !')
            return True
    return False

# fonction principale qui appelle les autres fonctions dans le bon ordre
def main():
    lettre = choixlettre()
    board = Jeu()
    rounds = 0
    while True:  # pour une boucle infinie
        displayBoard(board)
        if (rounds % 2 == 0):  # un coup sur deux
            play("X", board)
        else:
            play("0", board)
        if (gagnant(board)):
            break

        rounds += 1
        if (rounds == 9):  # match nul
            displayBoard(board)
            print('\nMatch nul !!')
            break

# fonction principale avec possibilité de recommencer une partie si les joueurs le souhaitent
main()
answer = str(input("\nVoulez-vous recommencer ? : "))
while (answer.lower() == "oui"):
    print('\n\n\n\n\n--- NOUVELLE PARTIE --- \n')
    main()
    answer = str(input("\nVoulez-vous recommencer ? : "))