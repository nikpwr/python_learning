# Kivi, sakset, paperi

lista = {'kivi','sakset','paperi'}

player1 = 'kivi'
player2 = 'sakset'

if player1 == player2:
    print('Tasapeli')
elif (player1 == 'kivi' and player2 == 'sakset') \
    or (player1 == 'sakset' and player2 == 'paperi') \
    or (player1 == 'paperi' and player2 == 'kivi'):
    print('Player 1 voittaa')  
else:
    print('Player 2 voittaa')
