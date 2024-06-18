vowels = ["A", "a", "E", "e", "I", "i", "O", "o", "U", "u"]

message = input("Input: ")
for char in message:
    if char in vowels:
        message = message.replace(char, "")
print("Output:", message)
