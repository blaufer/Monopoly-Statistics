from random import randrange

def community_chest(player,cc):
    comm_chest_cards = ['Advance to Go - Collect $200.',
        'Bank error in your favor – Collect $200.',
        'Doctors fees - Pay $50.',
        'From sale of stock you get $50.',
        'Get Out of Jail Free - This card may be kept until needed or \
            sold.',
        'Go to Jail - Go directly to jail – Do not pass Go – Do not \
            collect $200.',
        'Grand Opera Night – Collect $50 from every player for opening \
            night seats.',
        'Holiday Fund matures - Receive $100.',
        'Income tax refund – Collect $20.',
        'It is your birthday - Collect $10 from each player.',
        'Life insurance matures – Collect $100.',
        'Pay hospital fees of $100.',
        'Pay school fees of $150.',
        'Receive $25 consultancy fee.',
        'You are assessed for street repairs – $40 per house – $115 per \
            hotel.',
        'You have won second prize in a beauty contest – Collect $10.',
        'You inherit $100.']

    comm_def = [0,'x','x','x',10,'x','x','x','x','x','x','x','x','x','x',
        'x']

    if len(cc) == 0:
        cc = comm_def

    num = randrange(0,len(cc))

    if isinstance(cc[num],int):
        if cc[num] > 0:
            player = cc[num]
        else:
            player -= cc[num]
    elif isinstance(cc[num],str):
        player = player
    
    cc.pop(num)

    return player,cc
