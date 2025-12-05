with open("day2/input.txt", "r") as file:
    content = file.read()

ranges = content.split(",")

result = 0


def is_invalid_id(id: str) -> bool:
    mid = int(len(id) / 2)
    if id[:mid] == id[mid:]:
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
