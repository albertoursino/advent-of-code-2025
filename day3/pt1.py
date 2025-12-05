result = 0
with open("day3/input.txt", "r") as file:
    for line in file:
        line = line.strip()
        max_j = 0
        print(f"Processing line: {line}")
        for i in range(9, 0, -1):
            found = False
            for j in range(len(line)):
                if not found and j == len(line) - 1:
                    break

                n = int(line[j])
                if not found and n == i:
                    print(f"found {n} at position {j} for i={i}")
                    found = True
                    continue

                if found:
                    joltage = int(str(i) + str(n))
                    print(f"checking joltage {joltage}, calculate with {n} and {i}")
                    if joltage > max_j:
                        max_j = joltage

            if found:
                print(f"max_j for line {line} is {max_j}\n")
                result += max_j
                break

print(result)
