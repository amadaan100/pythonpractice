import re

email = input("Enter your email address: ").strip()

if re.search(r'.+@.+\..+', email):
#if re.search(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email):
    print("Valid email address.")
else:
    print("Invalid email address.")