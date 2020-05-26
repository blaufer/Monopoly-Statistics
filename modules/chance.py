from random import randrange

def chance(player,c):
    # All of the possible chance cards. There are two Advance to
    # nearest Railroad
    chance_cards = ['Advance to Go',
        'Advance to Illinois Ave. - If you pass Go, collect $200',
        'Advance to St. Charles Place – If you pass Go, collect $200',
        'Advance token to nearest Utility. If unowned, you may buy \
            it from the Bank. If owned, throw dice and pay owner a \
            total ten times the amount thrown.',
        'Advance token to the nearest Railroad and pay owner twice the \
            rental to which he/she is otherwise entitled. If Railroad \
            is unowned, you may buy it from the Bank.',
        'Advance token to the nearest Railroad and pay owner twice the \
            rental to which he/she is otherwise entitled. If Railroad \
            is unowned, you may buy it from the Bank.',
        'Bank pays you dividend of $50.',
        'Get out of Jail Free – This card may be kept until needed, or \
            traded/sold.',
        'Go Back 3 Spaces.',
        'Go to Jail – Go directly to Jail – Do not pass Go, do not \
            collect $200.',
        'Make general repairs on all your property – For each house pay \
            $25 – For each hotel $100.',
        'Pay poor tax of $15.',
        'Take a trip to Reading Railroad – If you pass Go, collect $200.',
        'Take a walk on the Boardwalk – Advance token to Boardwalk.',
        'You have been elected Chairman of the Board – Pay each player \
            $50.',
        'Your building loan matures – Collect $150.',
        'You have won a crossword competition - Collect $100.']

    chance_def = [0,24,11,[12,28],[5,15,25,35],[5,15,25,35],'x',-3,10,'x',
        'x',5,39,'x','x','x']

    if len(c) == 0:
        c = chance_def

    num = randrange(0,len(c))

    if isinstance(c[num],int):
        if c[num] > 0:
            player = c[num]
        else:
            player -= c[num]
    elif isinstance(c[num],list):
        for i in range(40):
            if (player + i) in c[num]:
                player += i
    elif isinstance(c[num],str):
        player = player

    c.pop(num)
    
    return player,c
