import random

board = [' ' for x in range(10)]

# mettre la lettre demandée à l'endroit demandé
def choixSigne(lettre, pos):
    board[pos] = lettre

# permet de voir si la zone spécifiée est libre
def espaceVide(pos):
    return board[pos] == ' '

# affiche le tableau
def displayBoard(board):
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ', board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ', board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ', board[9])
    print('   |   |')

# permet de savoir si la lettre X ou O a gagné
# en fonction des combinaisons gagnantes potentielles
def gagnant(board, lettre):
    return ((board[7] == lettre and board[8] == lettre and board[9] == lettre) or # alignement du bas
    (board[4] == lettre and board[5] == lettre and board[6] == lettre) or # alignement du milieu
    (board[1] == lettre and board[2] == lettre and board[3] == lettre) or # alignement du haut
    (board[7] == lettre and board[4] == lettre and board[1] == lettre) or # alignement gauche
    (board[8] == lettre and board[5] == lettre and board[2] == lettre) or # alignement milieu (colonne)
    (board[9] == lettre and board[6] == lettre and board[3] == lettre) or # alignement droit
    (board[7] == lettre and board[5] == lettre and board[3] == lettre) or # alignement diagonale
    (board[9] == lettre and board[5] == lettre and board[1] == lettre)) # alignement diagonale

# demande au joueur de choisir une position et si celle-ci n'est pas légitime
# continuera de demander jusqu'au bon choix
def playerJoue():
    run = True
    while run: # boucle jusqu'à ce que le choix soit validé
        joue = input('Choisissez une case pour placer un \'X\' (1-9): ')
        try:
            joue = int(joue)
            if joue > 0 and joue < 10: # pour assurer un choix entre 1 et 9
                if espaceVide(joue): # vérifie que l'emplacement est vide
                    run = False
                    choixSigne('X', joue)
                else:
                    print('Cette case est déjà occupée !')
            else:
                print('Choisissez un nombre entre 1 et 9 !')
        except:
            print('Choisissez un nombre !')

def ordiJoue(): # IA
# crée un liste de coups possibles
    possibleCoups = [x for x, lettre in enumerate(board) if lettre == ' ' and x != 0]
    joue = 0
    # vérifie si le coup est gagnant ou s'il faut bloquer l'adversaire gagnant
    for let in ['O', 'X']:
        for i in possibleCoups:
            boardCopy = board[:]
            boardCopy[i] = let
            if gagnant(boardCopy, let):
                joue = i
                return joue

    # essaie de prendre un des coins
    coinsOuverts = []
    for i in possibleCoups:
        if i in [1,3,7,9]:
            coinsOuverts.append(i)
    if len(coinsOuverts) > 0:
        joue = selectRandom(coinsOuverts)
        return joue

    # essaie de prendre le centre
    if 5 in possibleCoups:
        joue = 5
        return joue

    # prend un bord
    bordsOuverts = []
    for i in possibleCoups:
        if i in [2,4,6,8]:
            bordsOuverts.append(i)

    if len(bordsOuverts) > 0:
        joue = selectRandom(bordsOuverts)
    return joue

# choix au hasard de l'action à entreprendre
def selectRandom(li):
    ln = len(li)
    r = random.randrange(0, ln)
    return li[r]


# renvoie True si la grille est pleine et False si non
def boardFull(board):
    if board.count(' ') > 1:

        return False
    else:
        return True

# lance le jeu, appelle les fonctions et indique comment le jeu va fonctionner
def main():
    print('Bienvenue dans Tic Tac Toe')
    displayBoard(board)

    while not(boardFull(board)):
        if not(gagnant(board, 'O')):
            playerJoue()
            displayBoard(board)
        else:
            print('O\ est gagnant cette fois...')
            break

        if not(gagnant(board, 'X')):
            joue = ordiJoue()
            if joue == 0:
                print('Le jeu est à égalité ! On ne peut plus se déplacer.')
            else:
                choixSigne('O', joue)
                print('Ordi a placé un \'O\' dans la case', joue, ':')
                displayBoard(board)
        else:
            print('X\ gagne, bon travail !')
            break

    if boardFull(board):
        print('Le jeu est à égalité ! On ne peut plus se déplacer')

# pour redébuter le jeu ou pas
while True:
    answer = input('Encore une partie ? (O/N)')
    if answer.lower() == 'o' or answer.lower == 'oui':
        board = [' ' for x in range(10)]
        print('-----------------------------')
        main()
    else:
        break