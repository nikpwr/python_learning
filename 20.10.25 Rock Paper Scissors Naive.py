# Kivi, sakset, paperi

lista = {'kivi','sakset','paperi'}

player1 = 'kivi'
player2 = 'sakset'

if player1 == 'kivi':
    if player2 == 'kivi':
        print('Tasapeli')
    elif player2 == 'sakset':
        print('Player 1 voittaa')
    elif player2 == 'paperi':
        print('Player 2 voittaa')
elif player1 == 'sakset':
    if player2 == 'kivi':
        print('Player 2 voittaa')
    elif player2 == 'sakset':
        print('Tasapeli')
    elif player2 == 'paperi':
        print('Player 1 voittaa')
elif player1 == 'paperi':
    if player2 == 'kivi':
        print('Player 1 voittaa')
    elif player2 == 'sakset':
        print('Player 2 voittaa')
    elif player2 == 'paperi':
        print('Tasapeli')
