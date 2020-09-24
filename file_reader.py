pi_string = ''

with open("pi_digits.txt") as f:
    for line in f.readlines():
        pi_string += line

print(pi_string)
print(len(pi_string))

birthday = input("Enter Birthday format ddmmyy: ")

if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday dose not apper in the first million digits of pi.")
