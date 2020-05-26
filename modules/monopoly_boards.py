from operator import itemgetter

def monopoly_board():
    # Create the board as a list of lists and board_dict is used for 
    # output
    board = [[i,0] for i in range(0,40)]
    spaces = ['Go','Mediterranean Ave','Community Chest',
        'Baltic Avenue','Income Tax','Reading Railroad',
        'Oriental Ave','Chance','Vermont Ave','Connecticut Ave',
        'Jail','St. Charles Pl','Electric Company','States Ave',
        'Virginia Ave','Pennsylvania Railroad','St. James Place',
        'Community Chest','Tennessee Ave','New York Ave',
        'Free Parking','Kentucky Ave','Chance','Indiana Ave',
        'Illinois Ave','B & O Railroad','Atlantic Ave',
        'Ventnor Ave','Water Works','Marvin Gardens','Go To Jail',
        'Pacific Ave','North Carolina Ave','Community Chest',
        'Pennsylvania Ave','Short Line','Chance','Park Place',
        'Luxury Tax','Boardwalk']

    board_dict = {}

    for i in range(len(spaces)):
        board_dict[i] = spaces[i]

    return board, board_dict


def board_total(total,board):
    # Keeps a running total for all games played
    for i in range(len(board)):
        total[i][1] += board[i][1]

    return total


def pretty_print(board,board_dict):
    # Prints to the console
    count = 0

    for i in range(len(board)):
        count += board[i][1]

    for i in range(len(board)):
        board[i].append(board[i][1] / count)

    print('')
    print(' {0:>2s}  {1:<25s} {2:>8s}    {3:s}'.format(' ', 'Name', 
        'Total', 'Percent'))
    print('--------------------------------------------------')
    for i in range(len(board)):
        print(' {0:>2s}: {1:<25s} {2:8d}    {3:.4%}'.format(str(i),
            board_dict[i], board[i][1], board[i][2]))
    print('')

    board_sort = sorted(board, key=itemgetter(2), reverse=True)

    print(' {0:>2s}  {1:<25s} {2:>8s}    {3:s}'.format(' ', 'Name', 
        'Total', 'Percent'))
    print('--------------------------------------------------')
    for i in range(len(board_sort)):
        j = board_sort[i][0]
        print(' {0:>2s}: {1:<25s} {2:8d}    {3:.4%}'.format(str(j),
            board_dict[j], board_sort[i][1], board_sort[i][2]))
    print('')
