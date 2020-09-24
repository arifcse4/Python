pi_string = ''
with open("pi_digits.txt") as f:
    lines = f.readlines()
    for line in lines:
        pi_string += line.strip()

print(pi_string)
print(len(pi_string))