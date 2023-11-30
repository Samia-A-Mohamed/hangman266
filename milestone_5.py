
from Milestone_4 import Hangman

def play_game(word_list):
    num_lives = 5 
    game = Hangman(word_list, num_lives)
    while True:
      if game.num_lives == 0: 
        print ("You lost!") 
        break 
            
      elif game.num_lives !=0 and game.num_letters==0:
        print("Congratulations. You won the game!")
        break

      else: 
       game.ask_for_input()
        
    
    

play_game(["pinapple", "mango", "passionfruit", "lemon", "peach"])

