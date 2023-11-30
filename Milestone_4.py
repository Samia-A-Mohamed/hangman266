
#%%
import random

class Hangman:
    def __init__(self, word_list, num_lives = 0):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.word_guessed = ["_" for letter in self.word]
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []

    def check_guess(self, guess):
        guess = guess.lower()
        self.word = self.word.lower()
        if guess in self.word:
          print(f"Good guess! {guess} is in the word.")
          self.num_letters = self.num_letters - 1
          for index, letter in enumerate(self.word):
             if letter == guess:
                self.word_guessed[index] = guess
          print(self.word_guessed)
        else: 
          self.num_lives -= 1
          print(f"Sorry, {guess} is not in the word, try again!")
          print(f"You have {self.num_lives} lives left.")



    def ask_for_input(self):
      guess = input("Enter a single letter:") 
      if not guess.isalpha() or len(guess)!=1:  
         print("Invalid letter. Please, enter a single alphabetical character.")

      elif guess in self.list_of_guesses:
         print("You already tried that letter!")
         self.list_of_guesses.append(guess)
         print(self.list_of_guesses)

      else: 
         self.check_guess(guess)
         self.list_of_guesses.append(guess)

if __name__=="__main__":
   game = Hangman(["pinapple", "mango","passionfruit", "lemon", "peach"])
   game.ask_for_input()





           

# %%
