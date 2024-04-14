print("**RANDON PASSWORD GENERATOR**")

import random
import string

pass_len = int(input("Enter the length of password you want: "))
charValue = string.ascii_letters + string.digits + string.punctuation

        # list comprehension method

# password = "".join([random.choice(charValue) for i in range(pass_len)])

# print("Your random password is: ", password)

        # normal method

password = ""
for i in range(pass_len):
    password += random.choice(charValue)

print("Your random password is: ",password)