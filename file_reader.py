file_name = 'pi_digits.txt'

with open(file_name) as f:
    lines = f.readlines()

pi_string = ''

for line in lines:
    pi_string += line.strip()

print(len(pi_string))

birthday = input("Enter Birthday(ddmmyy): ")

if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!!!")
else:
    print("Your birthday does not appear in the first million digits fo pi.")

