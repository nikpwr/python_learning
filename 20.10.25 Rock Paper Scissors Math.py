# Kivi, sakset, paperi
# Mathmatical is the most optimised coding solution for this game
# Mapping three playing inputs to 0,1,2 and two players. 
LISTA = ['kivi','sakset','paperi']
INITIALS = ['k','s','p']

def get_answer(name):
    while True:
        answer = input(f'{name}: [K]ivi, [S]akset tai [P]aperi? ').lower()
        if answer in LISTA+INITIALS:
            return (LISTA+INITIALS).index(answer) % 3
        print('Väärä vastaus')

def play(player1,player2):
    if player1 == player2:
        print('Tasapeli')
    elif (player1 + 1) % 3 == player2: # inputs needed, numbers based on a mathematical analysis of potential results
        print('Player 1 voittaa')
    else:
        print('Player 2 voittaa')

player1 = get_answer('Player 1')
player2 = get_answer('Player 2')

play(player1,player2)

    # if answer1 in LISTA:
    #     player1 = LISTA.index(answer1)
    # else:
    #     player1 = INITIALS.index(answer1)

# while True:
#     answer2 = input('Player 2: [K]ivi, [S]akset tai [P]aperi? ').lower()
#     if answer2 in LISTA+INITIALS:
#         break
#     print('Väärä vastaus')

# if answer2 in LISTA:
#     player2 = LISTA.index(answer2)
# else:
#     player2 = INITIALS.index(answer2)


# player1 = 0
# player2 = 1
