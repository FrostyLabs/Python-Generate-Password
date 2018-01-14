# Script:  random_password.py
# Desc:    generates random password
# Author:  Oliver Thornewill
# Created: 2/10/16

import random

charset="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
charset+=charset.lower()   # This adds lower case letters to the charset
charset+="@&%_$#" # Add some Special Characters to the charset 
charset+="1234567890" # this adds numbers to the charset

def generate_password(length):
    """This function generates a random password."""
    password=[]
    length=raw_input('Specify how many characters you want your password to be:\n' )
    for n in range(int(length)):
        password.append(random.choice(charset))

    result ='' # initiates a result
    for item in password: 
        result += item # adds the next letter to the previous one recursively 
    
    return result

def main():
    # test cases
    print generate_password(generate_password)


# boilerplate that calls main() if run as script
if __name__ == '__main__':
    main()

