with open("pi_digits.txt") as f:
    lines = f.readlines()
    for line in lines:
        print(line.strip())
        