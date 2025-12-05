result = 0
with open("day3/input.txt", "r") as file:
    for line in file:
        line = line.strip()
        max_j = ""
        pointer = 0
        count = 0
        while count < 12:
            i = 9
            found = False
            while not found:
                for j in range(pointer, len(line) + 1 - (12 - count)):
                    if line[j] == str(i):
                        max_j += str(i)
                        pointer = j + 1
                        count += 1
                        found = True
                        i = 9  # reset i to 9 for next search
                        break
                if not found:
                    i -= 1

        result += int(max_j)
        print(f"max_j for line {line} is {max_j}\n")

print(result)
