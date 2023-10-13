import random
from time import time
import colorama
from colorama import Fore, Style

import os
os.system("cls||clear")

print(f"{Fore.LIGHTCYAN_EX}{Style.BRIGHT}Welcome to NumbrGuessr, Input a number you want to guess from (0 to #) \n{Fore.LIGHTWHITE_EX}{Style.NORMAL}")

numbr = int(input(f"{Fore.LIGHTCYAN_EX}Input number here: {Fore.LIGHTWHITE_EX}"))
genNum = random.randint(0, numbr)
guesses = 0

while True:
    
    startTime = time()
    guess = int(input(f"Guess Here: {Fore.LIGHTWHITE_EX}"))
    elapsedTime = time() - startTime
    
    stats = (f"{Fore.LIGHTGREEN_EX}You got the number in {guesses} guesses, with a time of {elapsedTime}!{Fore.LIGHTWHITE_EX}")
    
    if guess == genNum:
        print(stats)
        break
    elif guess > genNum:
        guesses += 1
        print(f"{Fore.YELLOW}{Style.BRIGHT}You're above the number{Fore.LIGHTWHITE_EX}{Style.NORMAL}")
    elif guess < genNum:
        guesses += 1
        print(f"{Fore.YELLOW}{Style.BRIGHT}You're below the number{Fore.LIGHTWHITE_EX}{Style.NORMAL}")
    else:
        print(f"{Fore.RED}{Style.DIM}ERROR{Style.NORMAL}")
        break
    
     