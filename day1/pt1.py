password = 0
actual_number = 50
with open("day1/input.txt", "r") as file:
    for line in file:
        line = line.strip()
        d = line[:1]
        c = int(line[1:])

        if d == "R":
            actual_number = (actual_number + c) % 100
        else:
            actual_number = (actual_number - c) % 100

        if actual_number == 0:
            password += 1

print(f"Password: {password}")
