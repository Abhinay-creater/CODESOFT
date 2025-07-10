print_board()
winner = check_winner(board)
if winner == 'X':
    print("Player 1 wins!")
elif winner == 'O':
    print("Player 2 wins!")
else:
    print("It's a tie!")
    
HERE
If you're assigning:

'X' → Player 1 (human)

'O' → Player 2 (AI)

Then this version will correctly show:

"Player 1 wins!" if the human wins

"Player 2 wins!" if the AI wins

"It's a tie!" for a draw
