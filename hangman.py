import random


from hangman_words import word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

lives = 6

from hangman_art import logo,stages
print(logo)
#testing code
print(f'pssst the solution is {chosen_word}.')

#create blanks
display = []
for _ in range(word_length):
    display += "_"
print(display)
end_of_game = False      

while not end_of_game:
    guess = input("guess a letter: ").lower()
#check guessed letter 
    for position in range(word_length):
        letter = chosen_word[position]
        #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
             display[position] = letter
    
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose")


#Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")


#Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")


    print(stages[lives])