"""This module covers the topics of conditionals and looping, including
some more topics like sleep function, random etc., making an 
ATM Simulator where the user can deposit or withdraw cash.
"""

__author__ = "Jashandeep Singh"
__version__ = "1.0.0"

import random
import time
import os

MAX_WIDTH = 40
FILL_CHARACTER = " "
menu_options = ["D", "W", "Q"]

user_balance = random.randint(-1000, 10000)
stars_filler = "".center(MAX_WIDTH, "*")

show_display = True

while show_display:
    # Initial Display
    print(stars_filler)
    print("PIXELL RIVER FINANCIAL".center(MAX_WIDTH, FILL_CHARACTER))
    print("ATM Simulator\n".center(MAX_WIDTH, FILL_CHARACTER))
    print(f"Your current balance is: ${user_balance:,.2f}\n".center(MAX_WIDTH, FILL_CHARACTER))
    print("Deposit: D".center(MAX_WIDTH, FILL_CHARACTER))
    print("Withdraw: W".center(MAX_WIDTH, FILL_CHARACTER))
    print("Quit: Q".center(MAX_WIDTH, FILL_CHARACTER))
    print(stars_filler)

    # Selection options
    selection = input("Enter your selection: ").capitalize()
    if selection not in menu_options:
        print()
        print(stars_filler)
        print("INVALID SELECTION".center(MAX_WIDTH, FILL_CHARACTER))
        print(stars_filler)
    elif selection == "Q":
        show_display = False
    elif selection == "D":
        transaction_amount = float(input("Enter the transaction amount: "))
        user_balance += transaction_amount
    elif selection == "W":
        transaction_amount = float(input("Enter the transaction amount: "))
        if user_balance >= transaction_amount:
            user_balance -= transaction_amount
        else:
            print()
            print(stars_filler)
            print("INSUFFICIENT FUNDS!".center(MAX_WIDTH, FILL_CHARACTER))
            print(stars_filler)

    print()
    print(stars_filler)
    print(f"Your current balance is: {user_balance:,.2f}".center(MAX_WIDTH, FILL_CHARACTER))
    print(stars_filler)

    # Wait for 3 seconds and clear display.
    time.sleep(3)
    os.system('cls' if os.name == 'nt' else 'clear')
