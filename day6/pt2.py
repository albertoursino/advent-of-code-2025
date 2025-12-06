from pathlib import Path

content = []
with Path("day6/input.txt").open() as f:
    for line in f:
        content.append([x for x in line])

last_row = content[-1]
content.pop(-1)

math_problems_info = []
counting = False
last_e = None
i = 0
for e in last_row:
    if e in ["+", "*"]:
        if not counting:
            counting = True
        else:
            math_problems_info.append((i - 1, last_e))
        i = 1
        last_e = e
    elif e == " " and counting:
        i += 1

math_problems_info.append((i, last_e))

# print(f"{math_problems_info=}")

math_problems = {}

for row in content:
    # print(f"Processing row: {row}")
    pointer = 0
    for i in range(len(math_problems_info)):
        if i not in math_problems:
            math_problems[i] = []
    for i, x in enumerate(math_problems_info):
        length, operator = x
        math_problems[i].append(row[pointer : pointer + length])
        pointer += length + 1

# print(f"{math_problems=}")

result = 0

for key in math_problems:
    op = math_problems_info[key][1]
    nums = []
    i = len(math_problems[key][0])
    while i > 0:
        num = ""
        for l in math_problems[key]:
            num += l[i - 1]
        i -= 1
        nums.append(int(num))

    if op == "+":
        result += sum(nums)
    elif op == "*":
        prod = 1
        for n in nums:
            prod *= n
        result += prod

print(result)
