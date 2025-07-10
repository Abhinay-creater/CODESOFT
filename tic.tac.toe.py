import random

# Define the board
board = [' ' for _ in range(9)]

def print_board():
    print('\n'.join([
        f"{board[0]} | {board[1]} | {board[2]}",
        "---------",
        f"{board[3]} | {board[4]} | {board[5]}",
        "---------",
        f"{board[6]} | {board[7]} | {board[8]}"
    ]))

def check_winner(brd):
    winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8), 
                            (0, 3, 6), (1, 4, 7), (2, 5, 8),
                            (0, 4, 8), (2, 4, 6)]
    for combo in winning_combinations:
        if brd[combo[0]] == brd[combo[1]] == brd[combo[2]] != ' ':
            return brd[combo[0]]
    return None

def minimax(brd, depth, is_maximizing):
    winner = check_winner(brd)
    if winner == 'O':
        return 1
    elif winner == 'X':
        return -1
    elif ' ' not in brd:
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for i in range(9):
            if brd[i] == ' ':
                brd[i] = 'O'
                score = minimax(brd, depth + 1, False)
                brd[i] = ' '
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(9):
            if brd[i] == ' ':
                brd[i] = 'X'
                score = minimax(brd, depth + 1, True)
                brd[i] = ' '
                best_score = min(score, best_score)
        return best_score

def ai_move():
    best_score = -float('inf')
    move = 0
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(board, 0, False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                move = i
    board[move] = 'O'

def player_move():
    while True:
        move = input("Enter your move (1-9): ")
        if move.isdigit() and 1 <= int(move) <= 9:
            move = int(move) - 1
            if board[move] == ' ':
                board[move] = 'X'
                break
            else:
                print("That spot is taken.")
        else:
            print("Invalid input. Choose 1-9.")

# Game loop
while True:
    print_board()
    if check_winner(board) or ' ' not in board:
        break
    player_move()
    if check_winner(board) or ' ' not in board:
        break
    ai_move()

print_board()
winner = check_winner(board)
if winner == 'X':
    print("Player 1 wins!")
elif winner == 'O':
    print("Player 2 wins!")
else:
    print("It's a tie!")
