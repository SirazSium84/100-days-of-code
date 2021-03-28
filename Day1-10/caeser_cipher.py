from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(logo)
keep_going = "yes"


def caesar(text, shift, direction):
    if direction == "encode":
        cipher_text = ""
        if shift > len(alphabet):
            while shift > len(alphabet):
                shift = shift % 26
        for x in text:
            if x == " ":
                cipher_text += x
            elif x.isalpha():
                if x.isupper():
                    if alphabet.index(x.lower()) + shift > len(alphabet) - 1:
                        cipher_text += alphabet[alphabet.index(
                            x.lower()) + shift - 26].upper()
                    else:
                        cipher_text += alphabet[alphabet.index(
                            x.lower()) + shift].upper()
                else:
                    if alphabet.index(x) + shift > len(alphabet) - 1:
                        cipher_text += alphabet[alphabet.index(
                            x) + shift - 26]
                    else:
                        cipher_text += alphabet[alphabet.index(x) + shift]

            else:
                cipher_text += x
        print(f"The encoded text is {cipher_text}")
    elif direction == "decode":
        decoded_text = ""
        for x in text:
            if x == " ":
                decoded_text += x
            elif x.isalpha():
                if x.isupper():
                    if alphabet.index(x.lower()) - shift < 0:
                        decoded_text += alphabet[alphabet.index(
                            x.lower()) - shift + 26].upper()
                    else:
                        decoded_text += alphabet[alphabet.index(
                            x.lower()) + shift].upper()
                else:
                    if alphabet.index(x) - shift < 0:
                        decoded_text += alphabet[alphabet.index(
                            x) - shift + 26]
                    else:
                        decoded_text += alphabet[alphabet.index(x) - shift]

            else:
                decoded_text += x
        print(f"The decoded text is {decoded_text}")


while keep_going == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n")
    shift = int(input("Type the shift number:\n"))
    caesar(text, shift, direction)
    keep_going = input(
        "Type 'yes' if you want to go again. Otherwise type 'no'\n").lower()
    if keep_going == "no":
        print("Good Bye!")
