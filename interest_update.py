"""Documentation"""

__author__ = "Jashandeep Singh"
__version__ = "1.0.0"

import csv
import pprint

customer_balances = {

}

file = open("account_balances.txt", "r")

with open('account_balances.txt', 'r') as file:
    reader = csv.DictReader(file)
    with open("account_balances.txt", "r") as file:
        for line in file:
            account_number, balance = line.strip().split("|")
            customer_balances[account_number] = float(balance)

pprint.pprint(customer_balances)

interest_earned = {}

for account, balance in customer_balances.items():
    if balance < 0:
        interest_rate = 0.10
    elif balance < 1000:
        interest_rate = 0.01
    elif balance < 5000:
        interest_rate = 0.025
    else:
        interest_rate = 0.05

    interest_amount = (balance * interest_rate) / 12

    interest_earned[account] = interest_rate

pprint.pprint(interest_earned)