from colorama import init as colorama_init
from colorama import Fore
from colorama import Style

colorama_init()

print(f"This is {Fore.RED}color{Style.RESET_ALL}!")

import re

# Regular expression pattern for Turkish phone numbers without +90 country code
pattern = r'^\(?0[1-9][0-9]{2}\)?[-.\s]?\d{3}[-.\s]?\d{2}[-.\s]?\d{2}$'

# Test phone numbers
phone_numbers = [
    "(123) 456-78-90",
    "05554443222",
    "555 444 33 22",
    "0212-345-67-89",
    "212.345.67.89"
]

for phone_number in phone_numbers:
    if re.match(pattern, phone_number):
        print(f"{phone_number} is a valid Turkish phone number without +90.")
    else:
        print(f"{phone_number} is not a valid Turkish phone number without +90.")

