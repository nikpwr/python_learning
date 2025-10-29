# Hangman
hidden_word = 'hirsipuu'
resolved_word = ['_'] * len(hidden_word)

while resolved_word.count('_'):
    print(''.join(resolved_word))
    user_letter = input('Kirjain?' )
    for index, word_letter in enumerate(hidden_word):
        if user_letter == word_letter:
            resolved_word[index] = user_letter
print(f'Voitit: {hidden_word}')