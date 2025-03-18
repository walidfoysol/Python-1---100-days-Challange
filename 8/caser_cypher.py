import art


alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]
def caesar_cypher(plain_text, shift_amount):
    message = ""
    for letter in plain_text:
        if letter not in alphabet:
            message += letter 
        else:
            position = alphabet.index(letter)
            new_position = position + shift_amount
            new_position = new_position%26
            new_letter = alphabet[new_position]
            message += new_letter
    return message

while True: 
    print(art.logo)
    direction = input("type 'encode' to encrypt and type 'decode' to decrypt the message:\n").lower()
    text = input("Type your message: \n")
    shift = int(input("Type the shift number:\n"))
    if direction == "encode":
        print(f"The encrypted message is {caesar_cypher(text,shift)}") # type: ignore
    else:
        shift *= -1
        print(f"The decrypted message is {caesar_cypher(text,shift)}") # type: ignore

    restart = input("Do you want to restart the program?")
    if restart != "yes":
        print("Goodbye! Thanks for using the cipher.")
        break




    





