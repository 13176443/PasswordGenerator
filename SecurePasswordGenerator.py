## Secure Password/Passphrase Generator v1.0 ##
# Authors: Sebastian Baszczyj   - 13176443@gordontafe.edu.au
#          Phoebe Cooney        - 13235673@gordontafe.edu.au
#
#    v1.0 - initial completion

# import the required modules
import secrets
import string
import random

# define the function which will generate the passwords
def generate_password():
    # Main loop keep in loop to ensure a password has been generated
    while True:
        try:
            # loop till given length variable is an integer value
            while True:
                try:
                    length = int(input("Enter the desired password length: "))
                    # if variable is 0 print and continue the loop till input is greater than 0 and break out of loop
                    if length == 0:
                        print("Please choose a length which is more than 0")
                        continue
                    break
                except ValueError:
                    print("Please enter a integer number")

# declare and assign variables for the inputs and characters variable
# below are while loops that loop until the input is yes or no and do something, if invalid it'll loop over to ask again
            characters = ''
            while True:
                uppercase = input("Include uppercase letters? (yes/no): ").lower()
                if uppercase == 'yes': # if yes add uppercase letters and end loop
                    characters += string.ascii_uppercase
                    break
                elif uppercase == 'no': # if no don't add uppercase letters and end loop
                    break
                else:   # if response is invalid continue loop again
                    print("Input must be (yes/no)")
                    continue

            while True:
                lowercase = input("Include lowercase letters? (yes/no): ").lower()
                if lowercase == 'yes':  # if yes add lowercase letters and end loop
                    characters += string.ascii_lowercase
                    break
                elif lowercase == 'no': # if no don't add lowercase letters and end loop
                    break
                else:   # if response is invalid continue loop again
                    print("Input must be (yes/no)")
                    continue

            while True:
                number = input("Include numbers? (yes/no): ").lower()
                if number == 'yes': # if yes add numbers and end loop
                    characters += string.digits
                    break
                elif number == 'no': # if no don't add numbers and end loop
                    break
                else:   # if response is invalid continue loop again
                    print("Input must be (yes/no)")
                    continue

            while True:
                symbol = input("Include symbols? (yes/no): ").lower()
                if symbol == 'yes': # if yes add symbols and end loop
                    characters += string.punctuation
                    break
                elif symbol == 'no': # if no don't add symbols and end loop
                    break
                else:   # if response is invalid continue loop again
                    print("Input must be (yes/no)")
                    continue

            # loop till given amount is an integer value
            while True:
                try:
                    amount = int(input("How many passwords would you like to generate? "))
                    # if variable is 0 print and continue the loop till input is greater than 0 and break out of loop
                    if amount == 0:
                        print("Please choose an amount which is more than 0")
                        continue
                    break
                except ValueError:
                    print("Please enter a correct integer number")
            # if true printed results will be outputted
            while True:
                output = input("Output results to a text file? (yes/no): ").lower()
                if output == 'yes':
                    break
                elif output == 'no':
                    break
                else:
                    print("Input must be (yes/no)")
                    continue

            # loop how many times a generated password is displayed based on the amount variable
            for i in range(amount):
                # join all choices in characters variable to password variable and print it
                password = ''.join(secrets.choice(characters) for _ in range(length))
                print("Generated password:", password)
                # if true printed results will be outputted to a text file called password.txt
                if output:
                    with open("passwords.txt", "a") as f:
                        print(password, file=f)
            # print on screen to notify the user their passwords have outputted to a text file
            if output == 'yes':
                print("Your password(s) have been saved into 'passwords.txt' in this scripts directory.")
            break
            # if no password has been generated don't break out of the loop, display a message and try again
        except IndexError:
            print("No password has been generated, try again:")

# define a word list required to generate a passphrase
wordlist = [
        "apple", "banana", "cherry", "dog", "elephant",
        "fish", "grape", "horse", "icecream", "jungle",
        "goat", "cow", "cat", "cake", "cookie", "trees",
        "stone", "wood", "gold", "house", "town", "street",
        "computer", "fridge", "gym", "chair", "couch"
    ]

# create the function which will generate passphrases
def generate_passphrase():
    # loop till given input is an integer value
    while True:
        try:
            words = int(input("Enter the number of words in the passphrase: "))
            # if variable is 0 print and continue the loop till input is greater than 0 and break out of loop
            if words == 0:
                print("Please choose a number of words which is greater than 0")
                continue
            break
        except ValueError:
            print("Please enter a integer number")
    # loop till given numbers variable is an integer value
    while True:
        try:
            numbers = int(input("Enter the amount of numbers between each word: "))
            break
        except ValueError:
            print("Please enter a integer number")

    # below are while loops that loop until the input is yes or no and do something, if invalid it'll loop over to ask again
    while True:
        capwords = input("Capitalize each word? (yes/no): ").lower()
        if capwords == 'yes':
            break
        elif capwords == 'no':
            break
        else:
            print("Input must be (yes/no)")
            continue

    # if yes set random capitalization
    while True:
        randcap = input("Random capitalization? (yes/no): ").lower()
        if randcap == 'yes':
            break
        elif randcap == 'no':
            break
        else:
            print("Input must be (yes/no)")
            continue

    # loop till given amount variable is an integer value
    while True:
        try:
            amount = int(input("Amount of passphrases would you like to generate? "))
            # if variable is 0 print and continue the loop till input is greater than 0 and break out of loop
            if amount == 0:
                print("Please choose an amount which is more than 0")
                continue
            break
        except ValueError:
            print("Please enter a integer number")

    # if true printed results will be outputted
    while True:
        output = input("Output results to a text file? (yes/no): ").lower()
        if output == 'yes':
            break
        elif output == 'no':
            break
        else:
            print("Input must be (yes/no)")
            continue

    # loop how many times a generated passphrase is displayed based on the amount variable
    for i in range(amount):
        passphrase = ''
        for i in range(words):
            # choose a random word(s) from the word list to the word variable based on the amount by the words variable
            word = random.choice(wordlist)
            # capitalize the words if true
            if capwords == 'yes':
                word = word.capitalize()
                # randomize the words if true
            if randcap == 'yes':
                word = ''.join(random.choice((str.upper, str.lower))(i) for i in word)
                # add the word to the passphrase
            passphrase += word
            # join the numbers variable to the passphrase and print the results
            if i < words - 1:
                passphrase += ''.join(str(random.randint(0, 9)) for _ in range(numbers))
        print("Generated passphrase:", passphrase)
        # if true printed results will be outputted to a text file called passphrase.txt
        if output == 'yes':
            with open("passphrases.txt", "a") as f:
                print(passphrase, file=f)
    # print on screen to notify the user their passwords have outputted to a text file
    if output == 'yes':
        print("Your passphrase(s) have been saved into 'passphrases.txt' in this scripts directory.")

# loop through to ask user to generate a 'password or 'passphrase' before executing the according function
while True:
    # ask the user to input whether they'd like to generate a password or passphrase and break the loop
    PASS = input("Generate a password or a passphrase? (password/passphrase) ")
    if PASS.lower() == 'password':
        generate_password()
        break
    elif PASS.lower() == 'passphrase':
        generate_passphrase()
        break
    else:
        print("Please input 'password' to generate a password or 'passphrase' to generate a passphrase")