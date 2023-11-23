
import random
word_list = ["pinapple", "mango", "passionfruit", "lemon", "peach"] 
word = random.choice(word_list)
print(word)

def check_guess(guess):
      guess.lower()
      if guess in word:
            print(f"Good guess! {guess} is in the word.")
      else: 
         print(f"Sorry, {guess} is not in the word, try again!")

def ask_for_input():
    guess = input("Enter a single letter:") 
    check_guess(guess)
    while True:
        guess = input("Enter a single letter:") 
        if guess.isalpha():
                break
        else:
           print("Invalid letter. Please, enter a single alphabetical character.")
ask_for_input()
     
