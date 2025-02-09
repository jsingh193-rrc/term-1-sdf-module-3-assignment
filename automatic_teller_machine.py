import random

MAX_WIDTH = 40
FILL_CHARACTER = " "
menu_options = {
    "D": "Deposit",
    "W": "Withdraw",
    "Q": "Quit"
}

user_balance = random.randint(-1000, 10000)
# print(user_balance)

print("****************************************".center(MAX_WIDTH, FILL_CHARACTER))
print("PIXELL RIVER FINANCIAL".center(MAX_WIDTH, FILL_CHARACTER))
print("ATM Simulator\n".center(MAX_WIDTH, FILL_CHARACTER))
print(f"Your current balance is: ${user_balance:,.2f}\n".center(MAX_WIDTH, FILL_CHARACTER))
print("Deposit: D".center(MAX_WIDTH, FILL_CHARACTER))
print("Withdraw: W".center(MAX_WIDTH, FILL_CHARACTER))
print("Quit: Q".center(MAX_WIDTH, FILL_CHARACTER))
print("****************************************".center(MAX_WIDTH, FILL_CHARACTER))