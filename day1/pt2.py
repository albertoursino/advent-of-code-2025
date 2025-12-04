from utils import pass_from_zero


password = 0
actual_number = 50
with open("day1/input.txt", "r") as file:
    for line in file:
        line = line.strip()
        d = line[:1]
        c = int(line[1:])

        password += pass_from_zero(actual_number, d, c)

        if d == "R":
            actual_number = (actual_number + c) % 100
        else:
            actual_number = (actual_number - c) % 100

print(f"Password: {password}")
