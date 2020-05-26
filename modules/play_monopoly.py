from random import randrange
from modules.chance import chance
from modules.community_chest import community_chest

def dice_roll():
    die_1 = randrange(1,7)
    die_2 = randrange(1,7)

    return die_1, die_2

def move(board,player,roll,c,cc):
    # Space landed on and if greater than Boardwalk, round the corner
    player += roll
    if player > 39:
        player %= 40

    # Add the move to the board totals
    board[player][1] += 1 
    # If added after going to jail, chance, etc, Jail becomes >8%

    # Landed on Go To Jail so move to Jail
    if player == 30:
        player = 10
        board[player][1] += 1
    # Landed on chance
    elif player in [7,22,36]:
        player,c = chance(player,c)
        board[player][1] += 1
    # Landed on community chest
    elif player in [2,17,33]:
        player,cc = community_chest(player,cc)
        board[player][1] += 1

    return board,player,c,cc

def roll(board,player,c,cc):
    # Track number of rolls
    count = 0

    while count < 2:
        # Roll two die
        die1,die2 = dice_roll()
        roll = die1 + die2

        board,player,c,cc = move(board,player,roll,c,cc)

        if die1 == die2:
            count += 1
        else:
            return board,player,c,cc

    # Go to jail on third double roll
    player = 10
    board[player][1] += 1

    return board,player,c,cc
