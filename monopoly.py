import os,sys
from random import randrange
from modules.monopoly_boards import *
from modules.play_monopoly import *


if __name__ == '__main__':
    total = [[i,0] for i in range(0,40)]

    # Number of games played
    num_games = 1000

    while num_games != 0:
        # Create a board with no moves
        board, board_dict = monopoly_board()

        # Create player(s) at 'Go'
        player_1 = 0

        # Create empty decks
        c = []
        cc = []

        # Number of moves
        moves = 100    

        while moves != 0:
            # Move player 1
            board, player_1, c, cc = roll(board,player_1,c,cc)

            moves -= 1

        num_games -= 1

        # Adds all the games together to get a 
        # grand total
        total = board_total(total,board)

    # Prints the results
    pretty_print(total,board_dict)
