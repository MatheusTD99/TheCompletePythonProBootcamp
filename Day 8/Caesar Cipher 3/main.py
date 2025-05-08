# TODO-1: Import and print the logo from art.py when the program starts.


#alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# TODO-2: What happens if the user enters a number/symbol/space?


#def caesar(original_text, shift_amount, encode_or_decode):
 #   output_text = ""
#      if encode_or_decode == "decode":
 #           shift_amount *= -1
#
    #    shifted_position = alphabet.index(letter) + shift_amount
   #     shifted_position %= len(alphabet)
  #      output_text += alphabet[shifted_position]
 #   print(f"Here is the {encode_or_decode}d result: {output_text}")


# TODO-3: Can you figure out a way to restart the cipher program?


#direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
#text = input("Type your message:\n").lower()
#shift = int(input("Type the shift number:\n"))

#caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)


import art
print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(original_text, shift_amount):
    encrypted_text = ""
    for letter in original_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = (position + shift_amount) % 26
            encrypted_text += alphabet[new_position]
        else:
            encrypted_text += letter
    print(f"The encrypted text is: {encrypted_text}")

def decrypt(original_text, shift_amount):
    decrypted_text = ""
    for letter in original_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = (position - shift_amount) % 26
            decrypted_text += alphabet[new_position]
        else:
            decrypted_text += letter
    print(f"The decrypted text is: {decrypted_text}")

# Loop para reiniciar o programa
should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if direction == "encode":
        encrypt(text, shift)
    elif direction == "decode":
        decrypt(text, shift)
    else:
        print("Invalid option. Please type 'encode' or 'decode'.")

    restart = input("Type 'yes' to go again. Otherwise, type 'no':\n").lower()
    if restart != 'yes':
        should_continue = False
        print("Goodbye!")





