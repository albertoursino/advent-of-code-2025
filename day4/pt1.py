from pathlib import Path


wall = []

with Path("day5/input.txt").open() as f:
    for line in f:
        wall.append([x for x in line.strip()])

result = 0
for i in range(len(wall)):  # rows
    for j in range(len(wall[i])):  # columns
        if wall[i][j] == "@":
            count = 0
            if i - 1 >= 0 and wall[i - 1][j] == "@":  # check up
                count += 1
            if i + 1 < len(wall) and wall[i + 1][j] == "@":  # check down
                count += 1
            if j - 1 >= 0 and wall[i][j - 1] == "@":  # check left
                count += 1
            if j + 1 < len(wall[i]) and wall[i][j + 1] == "@":  # check right
                count += 1
            if i - 1 >= 0 and j - 1 >= 0 and wall[i - 1][j - 1] == "@":  # check up-left
                count += 1
            if i - 1 >= 0 and j + 1 < len(wall[i]) and wall[i - 1][j + 1] == "@":  # check up-right
                count += 1
            if i + 1 < len(wall) and j - 1 >= 0 and wall[i + 1][j - 1] == "@":  # check down-left
                count += 1
            if i + 1 < len(wall) and j + 1 < len(wall[i]) and wall[i + 1][j + 1] == "@":  # check down-right
                count += 1
            if count < 4:
                result += 1

print(result)
