with open("day2/input.txt", "r") as file:
    content = file.read()

ranges = content.split(",")

result = 0


def is_invalid_id(id: str) -> bool:
    for i in range(1, len(id)):
        to_check = id[:i]
        counts = id.count(to_check)
        if counts == len(id) / len(to_check):
            return True
    return False


for r in ranges:
    init = int(r.split("-")[0])
    end = int(r.split("-")[1])
    for i in range(init, end + 1):
        if is_invalid_id(str(i)):
            result += i
            # print(f"Invalid ID: {i}")

print(f"Result: {result}")
