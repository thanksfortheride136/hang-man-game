import random
word = ["hey", "there", "bucko"]

def greeting():
    selected_word = random.choice(word)
    word_length = len(selected_word)
    print("Welcome to hang man")
    print(f"Your selected word is {word_length} letters long.")
    return selected_word
    
def string_to_letters(selected_word):
    individual_letters = []
    for i in selected_word:
        individual_letters.append(i)
    print(individual_letters)       #remove in final
    return individual_letters
    
def user_guess(letter_strings):
    attempts = 5
    found_letter = False
    #while attempts > 0 and len(correct_letters) 
    user_guess_input = input("First Letter Guess: ")
    correct_letters = []
    if user_guess_input in letter_strings:
        found_letter = True
    else: 
        found_letter = False
        
    if found_letter is True:
        correct_letters.append(user_guess_input)
    else:
        attempts -= 1
    print(correct_letters) #remove in final
    print(attempts) #remove in final
    return attempts, correct_letters
    
def game_complete():
    #specify game over or win condition
    None

def main():
    #does while logicgo here
    while guess[0] > 0:
        greeting_fun = greeting()
        string_letters = string_to_letters(greeting_fun)
        guess = user_guess(string_letters)
    else:
        game_complete()

main()
