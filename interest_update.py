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
    for line in file:
        account_number, balance = line.strip().split('|')
        customer_balances[account_number] = float(balance)

pprint.pprint(customer_balances)