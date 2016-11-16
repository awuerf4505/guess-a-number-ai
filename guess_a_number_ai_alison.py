#Guess-A-Number AI
#
#Alison Wuerfel
#September 9, 2016

import random
import math
def start_screen():

    print(" _____                               _   _                 _               ")
    print("|  __ \                             | \ | |               | |              ")
    print("| |  \/_   _  ___  ___ ___    __ _  |  \| |_   _ _ __ ___ | |__   ___ _ __ ")
    print("| | __| | | |/ _ \/ __/ __|  / _` | | . ` | | | | '_ ` _ \| '_ \ / _ \ '__|")
    print("| |_\ \ |_| |  __/\__ \__ \ | (_| | | |\  | |_| | | | | | | |_) |  __/ |   ")
    print(" \____/\__,_|\___||___/___/  \__,_| \_| \_/\__,_|_| |_| |_|_.__/ \___|_|   ")
    print("                            Press ENTER to Begin                            ")                                                                                                                                                                            
    input()
    

def play():

 
  got_it = False
  tries = 1
  print("Hello! What is your name?")
  name = input()
  print("What do you want your low value to be?")
  low = input()
  low = int(low)
  print("What do you want your high value to be?")
  high = input()
  high = int(high)
  print("Ok " + name + " please think of a nummber from " + str(low) + " to " + str(high) + ".")
  print("Press ENTER to continue...")
  input()

  while got_it == False:
    guess = (high + low) // 2


    print()
    print("Is it " + str(guess) + ", " + name + "?")
    answer = input("Higher? Lower? Am I right?")
    print()
  
    if answer == 'higher' or answer == 'h':
        low = guess + 1
        tries = tries + 1
    elif answer == 'lower' or answer == 'l':
        high = guess - 1
        tries = tries + 1
    elif answer == 'yes' or answer == 'y':
        got_it = True
        print("I got it! You lost " + name + "!")
        print("It took me " + str(tries) + " try/tries to guess your number " + name + ".")
    else:
        print("What?! Just say higher, lower, or yes!")
        
      
  if got_it == True:
        print("Game Over")

def play_again():

    while True:
        answer = input("Would you like to play again?")

        if answer == 'no' or answer == 'n':
            return False
        elif answer == 'yes' or answer == 'y':
            return True
    
        print("What??!! Just say yes or no.")


# game begins
start_screen()
again = True
while again == True:
       play()
       again = play_again()



print("         _____      ___       ___  ___   _______")
print("        /  ___|    /   |     /   |/   | |   ____|") 
print("        | |       /    |    / /|   /| | |  |__")
print("        | |  _   /  /| |   / / |__/ | | |   __|")
print("        | |_| | /  ___ |  / /       | | |  |____")
print("        \_____//_/   |_| /_/        |_| |_______|")
        
print("         _____    _     _   ______   ______")
print("        /  _  \  | |   / / | _____| |  _   \\")
print("        | | | |  | |  / /  | |__    | |_|  |")
print("        | | | |  | | / /   |  __|   |  _   /")
print("        | |_| |  | |/ /    | |____  | | \  \\")
print("        \_____/  |___/     |______| |_|  \__\\")
print("By Alison W.")
print("Completed September 9, 2016")


 

    
    
 
    

