# Hangman
# I have done the drawing part for you since it took a lot of time to code
# the drawing of the man. It is up to you to put in the game logic

# game is a function that takes in the word as a parameter and runs the game of
# hangman. Inside the function are comments that give you hints about the code
# you need to write
def game(word):
    # you need variables for the number of guesses currently used and the total
    # number of guesses
    # variable here

    # you need a variable for the number of correct letters guessed
    # variable here

    # create a while loop (look a gameplan if you need help) that ends when
    # either the number of guesses has been reached or the number of correct
    # guesses equals the length of the word

    # while loop here HINT: word length can be done with len(word)

    # inside the while loop you need to prompt the user for a guess
    # HINT: the input function is useful here

    # then you need to check if the character is in the word HINT: if statement
    # check here

    # if the character is in the word add one to the number of correct guesses
    # if the character is not in the word add one to the guesses used

    # finally, return true or false depending on whether the word was guessed
    # correctly or the number of guesses has been reached

    # Also! Don't forget to call the draw function in the loop to draw the man!


def draw(guesses):
    man = [' O ','\\','|','/','/','\\']
    for part in range(0,guesses):
        if part > 0 and part < 4:
            print(man[part],end='')
            if part == 3:
                print()
        elif part == 4 or part == 5:
            print(man[part],end='')
        else:
            print(man[part])
    print()
# end
word = input('Type a word while the other person looks away! ')
res = game(word)
if res == True:
    print('The word was ' + word)
else:
    print('You lose! The word was ' + word)
