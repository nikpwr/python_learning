# Hirsipuu / Hangman using class / OOP

class Guessword:

    def __init__(self, hidden_word:str):
        self._hidden_word = hidden_word
        self._resolved_word = ['_'] * len(self._hidden_word)
        Guessword._VALID_LETTERS = 'abcdefghijklmnopqrstuvwzäö'
        self.used_letters = set() #It's better to use a set instead of a string because strings are immuttable and will create new pointers
        self._is_resolved = False

    def hidden_word(self) -> str:
        return(f"Arvattava sana on {''.join(self._resolved_word)}")

    def is_resolved(self)->bool:
        
        if self._resolved_word.count('_') == 0: #Are there an further letters to guess?
            self._is_resolved = True
            print(f'Voitit! Sana oli {self._hidden_word}')

        return self._is_resolved
        
    def resolve_letter(self,user_answer:str):

        match user_answer:
            case '0': #Player wants to exit
                print('Kiitos pelaamisesta')
                self._is_resolved = True
                return None
            case user_answer if (len(user_answer) == 1): #Player guessed a letter
                if user_answer in self.used_letters: 
                    print("Letter already answered")
                else:
                    self.used_letters.add(user_answer)
                for index, word_letter in enumerate(self._hidden_word):
                    if user_answer == word_letter:
                        self._resolved_word[index] = user_answer #Replace _ with guessed letter
            case user_answer if user_answer == self._hidden_word: #All letters have been guessed
                self._resolved_word = list(self._hidden_word)
    
    def ask_user(self, question: str) -> str:
        while True:
            answer = input(question).lower()
            match answer:
                case '':
                    continue
                case '0':
                    return '0'
                case _:
                    for letter in answer:
                        if letter not in Guessword._VALID_LETTERS:
                            break
                    else:
                        return answer

game = Guessword("hirsipuu")
while not (game.is_resolved()):
    print(game.hidden_word())
    letter = game.ask_user('Syötä kirjain tai sana (A-Za-zÄäÖö). 0->lopettaa peli\n' )
    game.resolve_letter(letter)
