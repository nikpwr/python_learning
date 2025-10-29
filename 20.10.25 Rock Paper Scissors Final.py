# Peli: Kivi, sakset, paperi 
LISTA = ['kivi','sakset','paperi']
INITIALS = ['k','s','p']

def get_answer(name: str):
    """
    Prompts the console for an answer for a player and checks the answer if valid. The player should answer Rock paper or scissors with k, s or P.
    Returns the remainder from modula 3 as an int if the answer is valid. 
    If the answer is not valid, it will ask again and print a message to the console asking for the answer again

    Parameters:
        name (string): Name of the player used for presentation.

    Returns:
        int: Modula 3 of users answer.
    """
    while True:
        answer = input(f'{name}: [K]ivi, [S]akset tai [P]aperi? ').lower()
        if answer in LISTA+INITIALS:
            return (LISTA+INITIALS).index(answer) % 3
        print('Väärä vastaus')

def play(player1:int,player2:int):
    """
    Checks out of which player has won of it there was a draw

    Parameters:
        player1 (int): Provide the result of modula output of player1 answer.
        player2 (int): Provide the result of modula output of player2 answer.
 
        player1 = get_answer('Player 1')
        player2 = get_answer('Player 2')
 
        play(player1,player2)
 
    Returns:
        None (None): No output, only prints to the console the game's result of the players answer.
    """
    if player1 == player2:
        print('Tasapeli')
    elif (player1 + 1) % 3 == player2: # inputs needed, numbers based on a mathematical analysis of potential results
        print('Player 1 voittaa')
    else:
        print('Player 2 voittaa')

player1 = get_answer('Player 1')
player2 = get_answer('Player 2')

play(player1,player2)