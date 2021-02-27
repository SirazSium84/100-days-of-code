import base64
string = "aHR0cHM6Ly9mb3Jtcy5nbGUvWU5ZXQ0d2NRWHVLNnNwdjU="
words_list = []
y = 0
for x in range(12):
    words_list.append(string[y:y+4])
    y += 4
print(words_list)
output = ""

for word in words_list:
    base64_message = word
    print(word)
    base64_bytes = base64_message.encode("ascii")
    message_bytes = base64.b64decode(base64_bytes)
    try:
        message = message_bytes.decode("ascii")
        output += message
    except UnicodeDecodeError:
        continue
print(output)
