import random
from words import words
from hangmanVisual import lives_visual_dict
import string

def get_valid_word(words):
    word=random.choice(words)
    while '-' in word or ' ' in word:   #ignores words with spaces or dashes (which can't be guessed in hangman)
        word=random.choice(words)
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) # letters in the word
    alphabet = set(string.ascii_uppercase) # all letters (upper case)
    used_letters = set() #what user has guessed

    lives=7


    print('Guess the word!')
    #getting user input 
    while len(word_letters)>0 and lives > 0:
        print('\nYou have ', lives ,' lives left. You have used these letters: ', ' '.join(used_letters))#turns used letters into string separated by ' '

        word_list = [letter if letter in used_letters else '-' for letter in word]
        print(lives_visual_dict[lives])
        print('Current word: ', ' '.join(word_list)) 

        user_letter=input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:#user guesses a letter that has never been guessed before
            used_letters.add(user_letter)
            if user_letter in word_letters:#user guesses a correct letter
                word_letters.remove(user_letter)
                print('Correct!')
            else:#if user guesses a new letter that is incorrect they lose a life, this does not decrease lives if a user repeats a used letter
                lives-=1
                print('Incorrect! letter is not in word')
        

        elif user_letter in used_letters:#user enters a letter, but they have entered it before
            print('You have already used this letter. Guess another letter')
        else:#user enters something that is not a letter
            print('you have entered an invalid character')

    if lives>0:
        print(f'\nCongrats! you guessed the word {word}')
        
    else:
        print(f'\nGame Over! Word was {word}')
        print(lives_visual_dict[lives])
    

#user_input = input('Type something')
hangman()