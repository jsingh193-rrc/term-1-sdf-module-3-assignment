"""Documentation"""

__author__ = "Jashandeep Singh"
__version__ = "1.0.0"

import csv
import pprint

customer_balances = {

}

file = open("account_balances.txt", "r")


with open("account_balances.txt", "r") as file:
    for line in file:
        account_number, balance = line.strip().split("|")
        customer_balances[account_number] = float(balance)

pprint.pprint(customer_balances)

for account, balance in customer_balances.items():
    if balance < 0:
        interest_rate = 0.10
    elif balance < 1000:
        interest_rate = 0.01
    elif balance < 5000:
        interest_rate = 0.025
    else:
        interest_rate = 0.05

    balance += ((balance * interest_rate) / 12)
    customer_balances[account] = balance

print("Update the balance balance after adding interest")
pprint.pprint(customer_balances)

filename = 'updated_balances_JS.csv'
with open(filename, "w", newline='') as csvfile:
    fieldnames = ['Account', 'Balance']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()

    for account_number, balance in customer_balances.items():
        writer.writerow({'Account': account_number, 'Balance': balance})