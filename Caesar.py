import string 

def caesar(text, shift, alphabets): # create a caesar method to shift the alphabet

    def shift_alphabet(alphabet):

        return alphabet[shift:] + alphabet[:shift] # returns the new shifted alphabet based on the shift inserted


    shiftedAlphabet = tuple(map(shift_alphabet, alphabets)) 

    finalAlphabet = ''.join(alphabets)

    finalShiftedAlphabet = ''.join(shiftedAlphabet)

    table = str.maketrans(finalAlphabet, finalShiftedAlphabet)

    return text.translate(table)



def decipher(text, shift, alphabets):

    def unshift_alphabet(alphabet):

        return alphabet[:shift] + alphabet[shift:] 

    unshiftedAlphabet = tuple(map(unshift_alphabet, alphabets))

    finalAlphabet = ''.join(alphabets)

    finalUnshiftedAlphabet = ''.join(unshiftedAlphabet)

    table = str.maketrans(finalAlphabet, finalUnshiftedAlphabet)

    return text.translate(table)



userChoice = input("\nDo you want to ENCRYPT or DECIPHER? ")

userChoice = userChoice.upper()


if (userChoice == "ENCRYPT"):

    userEncryption = input("\nWhat do you want to encrypt? ")

    userShift = int(input("\nWhat is the shift (1-25)? "))

    userShift %= 26

    print("\nEncrypting...\n")

    print(caesar(userEncryption, userShift, [string.ascii_lowercase, string.ascii_uppercase, string.punctuation]))

    print("\n")

    

elif(userChoice == "DECIPHER"):

    userCipher = input("\nWhat do you want to cipher? ")

    userShift = int(input("\nWhat is the shift? "))

    print("\nDeciphering...\n")

    print(decipher(userCipher, userShift, [string.ascii_lowercase, string.ascii_uppercase, string.punctuation]))

    print("\n")



else:
    print("\nAre you dumb? That wasn't an option\n")



# userInput = input("\nWhat do you want to encrypt? ")

# plain_text = "\n{userInput}\n" 

# print(caesar(plain_text, 7, [string.ascii_lowercase, string.ascii_uppercase, string.punctuation]))



#$bzlyPuwba&
