import random
# created a list of fruits 
word_list = ["pinapple", "mango", "passionfruit", "lemon", "peach"]
print(word_list)
# generate a random fruit from the word_list
word = random.choice(word_list)
print(word)
# asked the user to enter a single letter 
guess = input("Enter a single letter:")
# checked that the input is a single character 
length_of_input = len(guess)
if length_of_input == 1 and guess.isalpha():
    print("Good guess!")
else:
    print("Oops! That is not a valid input")
