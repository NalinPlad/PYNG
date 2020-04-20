import time
import random

print("PYNG V1.0 2020 by Piffle\n")
password = int(input("\nwhat is the passcode(currently only supports positive numbers greater than 0):    "))
guess = 0
guessed = False
timer = 0




while 1:

  guess = random.randrange(0, password+1)
  timer = timer + 1
  print(timer, ": guesses  ", guess, ": current guess")
  if guess == password:
      guessed = True
      print("got it, it was ", password, " after ", timer, " guesses") 
      quit()
