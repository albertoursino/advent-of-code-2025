from pathlib import Path


ranges = []
ids = []
with Path("day5/input.txt").open() as f:
    check = False
    for line in f:
        line = line.strip()
        if "-" in line:
            ranges.append(line)
        elif "" in line and not check:
            check = True
        elif check:
            ids.append(line)

result = 0
for id in ids:
    for r in ranges:
        start, end = map(int, r.split("-"))
        if start <= int(id) <= end:
            result += 1
            break

print(result)
