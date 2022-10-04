# File: Wordle.py
"""
pyWordle
IS 562 - Project Management - Hilton
Members: Chandler Taylor, Ali Smith, Michael Pisicone, David Jensen, Keanna Nebrotzky, Nathan Hansen
"""

import random
from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS


def wordle():
  # Set the secret word
  secretWord = random.choice(FIVE_LETTER_WORDS)
  print(secretWord)

  def increment_row(row):
    # Increment row if all guesses are not filled
    if row < 5:   
      row += 1
      gw.set_current_row(row)
    elif row == 5:
      gw.show_message(secretWord)
      # TODO: Add code here for LOSS end game state

  def color_letters(guess,row):
    i = 0
    for x, y in zip(guess, secretWord):
      if x==y:
        gw.set_square_color(row,i,"#66BB66")
        i+=1
      else:
        i+=1
        
  
  def enter_action(s):
    
    # gw.show_message("You have to implement this method.")
    #Milestone 1:
    # for x in range(N_ROWS):
    #   for y in range(N_COLS):
    #     gw.set_square_letter(x,y,secretWord[y])

    #Milestone 2:

    #Turn the user's input into a lowercase string
    rowNum = gw.get_current_row()
    # print(rowNum)
    userGuess = ""
    for x in range(N_COLS):
      userGuess = (userGuess + gw.get_square_letter(rowNum,x)).lower()

    #Compare userGuess to each word in word list
    inList = False
    for x in range(len(FIVE_LETTER_WORDS)):
      if userGuess == FIVE_LETTER_WORDS[x]:
        inList = True

    # Print secret word in console for testing
    #print(secretWord)
    
    #Show user if it is word list
    if inList == False:
      
      # Clear row and reset if userGuess isn't a valid word
      gw.show_message("Not in word list")
      
      for x in range(N_COLS):
        gw.set_square_letter(rowNum,x,'')
        
      gw.set_current_row(rowNum)
      
    elif inList == True and userGuess != secretWord:
      gw.show_message("In word list") 
      color_letters(userGuess, rowNum)
      increment_row(rowNum)   
      
    elif userGuess == secretWord:
      color_letters(userGuess, rowNum)
      gw.show_message("Congrats")
      # TODO: Add code here for WIN game state

  gw = WordleGWindow()
  gw.add_enter_listener(enter_action)


# Startup code
if __name__ == "__main__":
  wordle()
