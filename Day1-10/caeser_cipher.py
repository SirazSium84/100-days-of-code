alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

if direction == "encode":
    def encode(text, shift):
        output_text = ""
        for x in text:
            if x == " ":
                output_text += x
            elif alphabet.index(x) + shift > len(alphabet) - 1:
                output_text += alphabet[alphabet.index(x) + shift - 25]
            else:
                output_text += alphabet[alphabet.index(x) + shift]
        return output_text
    print(encode(text, shift))

else:
    def decode(text, shift):
        output_text = ""
        for x in text:
            if x == " ":
                output_text += " "
            elif alphabet.index(x) - shift < 0:
                output_text += alphabet[alphabet.index(x) - shift + 25]
            else:
                output_text += alphabet[alphabet.index(x) - shift]
        return output_text
    print(decode(text, shift))
