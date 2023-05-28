# Ceaser Cipher
# A simpler program to encryt and decrypt messages
# 26/05/2023

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(plan_text, shift_amount):
    """ Encrypts the user entered text by the given amounts of shift"""
    cipher_text = ""
    for letter in plan_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        new_letter = alphabet[new_position]
        cipher_text += new_letter

    print(f"the encoded text is: {cipher_text}")


encrypt(text, shift)
input("\n\nPress enter to exit.")
