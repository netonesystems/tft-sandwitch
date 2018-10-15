# demo.py

import pygame, pybutton, pymenu, sys, tetris
import tetris
import invader 
from constants import *

# this is a demo of how to use the pymenu and pybutton classes
# 1. initialize the menu class: pymenu.PyMenu()
# 2. create the buttons: pybutton.PyButton() 
# 3. add the buttons and their actions: menu.addButton()
# 4. draw the menu to the screen: menu.draw()

pygame.init()

# create your own button actions here
def callback(index):
  """ Just a stub """
  # in pymenu.py, the button index
  # will be passed to the function
  # you add below in addButton()

  # which means you can check
  # for the index like this:
  # if index == 1:
  #  tetris.main()
  if index == 1:
    invader.main()
  if index == 2:
    tetris.main()
  if index == 4:
    pygame.quit()
    sys.exit()
  
  # now it just prints the index
  print (index)

def setUpMenu():
  """ How to use the PyMenu and PyButton classes. """

  # create the window
  window = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
  pygame.display.set_caption("Games")
  
  # initialize the menu
  menu = pymenu.PyMenu(BLACK, WINDOWWIDTH/2, 45, "Games")
  
  # create the buttons
  backButton = pybutton.PyButton(WINDOWWIDTH/2, 100, "Back to Game")
  newButton = pybutton.PyButton(WINDOWWIDTH/2, 130, "New Game \"INVADER\"")
  challengeButton = pybutton.PyButton(WINDOWWIDTH/2, 160, "New Game \"TETRIS\"")
  aboutButton = pybutton.PyButton(WINDOWWIDTH/2, 190, "About")
  quitButton = pybutton.PyButton(WINDOWWIDTH/2, 220, "Quit")

  # add the button to the menu as the first argument
  # the second argument is the corresponding action
  # when the button is clicked, its action will be called
  
  # also don't forget to leave out the parenthesis after
  # the function name, as explained here:
  # http://stackoverflow.com/questions/1349332/python-passing-a-function-into-another-function
  # otherwise the function will be directly called
  # pass callback, not callback()
  menu.addButton(backButton, callback)
  menu.addButton(newButton, callback)
  menu.addButton(challengeButton, callback)
  menu.addButton(aboutButton, callback)
  menu.addButton(quitButton, callback)

  # draw the menu
  menu.draw(window)

if __name__ == '__main__':
  setUpMenu()
