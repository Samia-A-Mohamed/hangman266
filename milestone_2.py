import random
word_list = ["pinapple", "mango", "passionfruit", "lemon", "peach"] 

def random_word():
   word_list = ["pinapple", "mango", "passionfruit", "lemon", "peach"]
   word = random.choice(word_list)
   return word.upper
random_word()

guess = input("Enter a single letter:")
    
length_of_input = len(guess)

def user_guess():
    if length_of_input == 1 and guess.isalpha():
      print("Good guess!")
    else:
      print("Oops! That is not a valid input")

