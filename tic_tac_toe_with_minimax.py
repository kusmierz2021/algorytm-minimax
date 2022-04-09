from math import inf as infinity
from random import randint

player, opponent = 'x', 'o'
# player, opponent = 'o', 'x'

def availableMoves(state):
    # zwraca listę dostępnych ruchów
    available_moves = []
    for x, row in enumerate(state):
        for y, cell in enumerate(row):
            if cell == '_':
                available_moves.append([x,y])
    return available_moves


def isMoveLeft(state):
    # sprawdza, czy jest możliwość wykonania kolejnego ruchu
    for i in range(3):
        for j in range(3):
            if (state[i][j] == '_'):
                return True
    return False


def evaluate(state):
    # sprawdza czy jest stan terminalny
    for row in range(3):        # sprawdza wiersze
        if (state[row][0] == state[row][1] and state[row][1] == state[row][2] ):
            if (state[row][0] == player):
                return 10
            elif (state[row][0] == opponent):
                return -10

    for col in range(3):        # sprawdza kolumny
        if (state[0][col] == state[1][col] and state[1][col] == state[2][col]):
            if (state[0][col] == player):
                return 10
            if (state[0][col] == opponent):
                return -10
    # sprawdza obie przekątne
    if (state[0][0] == state[1][1] and state[1][1] == state[2][2]):
        if (state[0][0] == player):
            return 10
        elif (state[0][0] == opponent):
            return -10

    if (state[0][2] == state[1][1] and state[1][1] == state[2][0]):
        if (state[0][2] == player):
            return 10
        elif (state[0][2] == opponent):
            return -10
    return 0


def minimax(state, depth, isMax):
    # przyjmuje stan, głębokość oraz czy obecny gracz jest graczem maksymalizującym
    score = evaluate(state)
    if (score == 10):
        return (score - depth)
    if (score == -10):
        return (score + depth)
    if (isMoveLeft(state) == False):
        return 0

    available_moves = availableMoves(state)

    if (isMax):
        best = -infinity

        for available_move in available_moves:
            state[available_move[0]][available_move[1]] = player
            best = max(best, minimax(state, depth + 1, not isMax))
            state[available_move[0]][available_move[1]] = '_'
        return best

    else:
        best = infinity

        for available_move in available_moves:
            state[available_move[0]][available_move[1]] = opponent
            best = min(best, minimax(state, depth + 1, not isMax))
            state[available_move[0]][available_move[1]] = '_'
        return best


def findBestMove(state):
    # podpowiada graczowi najlepszy możliwy ruch w zadanym stanie
    # jeżeli player, opponent = 'x', 'o' podpowiada ruch dla x
    # jeżeli player, opponent = 'o', 'x' podpowiada ruch dla o
    print_board(state)

    score = evaluate(state)
    if (score == 10):
        print("%s has already won!" % player)
        return 0
    elif (score == -10):
        print("%s has already won!" % opponent)
        return 0
    elif (isMoveLeft(state) == False):
        print("it is draw already!")
        return 0


    print("the best move in that situation is:")
    bestVal = -infinity
    bestMove = (-1, -1)

    available_moves = availableMoves(state)
    for available_move in available_moves:
        state[available_move[0]][available_move[1]] = player
        moveVal = minimax(state, 0, False)
        state[available_move[0]][available_move[1]] = '_'

        if ((moveVal > bestVal) or (moveVal == bestVal and randint(0,1) == 0)):
            bestMove = (available_move[0], available_move[1])
            bestVal = moveVal


    state[bestMove[0]][bestMove[1]] = player
    print_board(state)
    state[bestMove[0]][bestMove[1]] = '_'
    return 0

def print_board(board):
    # wypisuje tablicę gry w konsoli
    for i in range(3):
        print("| %s | %s | %s |" % (board[i][0], board[i][1], board[i][2]))
