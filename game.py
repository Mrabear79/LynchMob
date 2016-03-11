import random
import linecache
import graphics
import time
import urllib.request

def main():
    print('H A N G M A N')
    missed_letters = ''
    correct_letters = ''
    secret_word = get_random_word()
    game_is_done = False

    while True:
        graphics.display_board(missed_letters,correct_letters,secret_word)
        letter_guess = get_letter(missed_letters+correct_letters)
        if letter_guess in secret_word:
            correct_letters += letter_guess
            found_word = True
            for x in range(len(secret_word)):
                if secret_word[x] not in correct_letters:
                    found_word = False
                    break
            if found_word:
                    print("Great job! The secret word is {word}! ".format(word=secret_word))
                    game_is_done = True
                    time.sleep(5)
        else:
            missed_letters += letter_guess
            print()
            print("Sorry! There was no {0}'s' in the word.".format(letter_guess))
            print()
        if len(missed_letters) == len(graphics.HANGMANPICS) - 1:

            graphics.display_board(missed_letters,correct_letters,secret_word)

            print()
            print("Sorry you lose! The word is {0}. ".format(secret_word))


            time.sleep(5)

            game_is_done = True


        if game_is_done:
            play_again = str(input("Would you like to play again? (Y)es ")).lower()
            if play_again == 'y' or play_again == 'yes':
                missed_letters = ''
                correct_letters = ''
                secret_word = get_random_word()
                game_is_done = False
            else:
                break


def get_letter(letters):
    alpha = "abcdefghijklmnopqrstuvwxyz"

    while True:
        letter_guess = str(input("Guess a letter. ")).lower()
        if letter_guess not in alpha:
            print("Not a relative choice. ")
            continue

        if letter_guess in letters:
            print("That letters been guessed already. ")
            continue
        return str(letter_guess).lower()


def count_lines():
    with open('words.txt') as f:
        for i, l in enumerate(f):
            pass

    return i + 1


def get_random_word():
    with urllib.request.urlopen("http://randomword.setgetgo.com/get.php") as response:
        word = response.read()
        print(word.decode('utf8'))
        return (word.decode('utf8'))


main()
