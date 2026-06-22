import random
import string

dict_path = '/usr/share/dict/words'
with open(dict_path, 'r') as f:
    words = [line.strip() for line in f]

def hangman():
    word = random.choice(words).upper()
    word_letters = set(word) # ['D','O','G']
    used_letters = set()
    alphabet =  set(string.ascii_uppercase)

    lives = 7
    while len(word_letters) > 0 and lives > 0:
        print('You have guessed these letters: ', ' '.join(used_letters))
        word_list =  [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ''.join(word_list))

        user_input = input('Guess a letter: ').upper()

        if user_input in alphabet - used_letters:
            used_letters.add(user_input)
            if user_input in word_letters:
                word_letters.remove(user_input)
            else:
                lives -= 1
                print('Letter not in word.')
        elif user_input in used_letters:
            print('You already guessed that letter.')
        else:
            print('Invalid input.')

    if lives == 0:
        print(f'You died. The word is {word}')
    else:
        print(f'🎉 You guessed the word: {word}')

hangman()
