from pathlib import Path


ranges = []
with Path("day5/input.txt").open() as f:
    check = False
    for line in f:
        line = line.strip()
        if "-" in line:
            ranges.append((int(line.split("-")[0]), int(line.split("-")[1])))
        elif "" in line:
            break

sorted_starts = sorted(ranges, key=lambda x: x[0])

process_ranges = []

while sorted_starts:
    r = sorted_starts.pop(0)
    start = r[0]
    end = r[1]
    merged_range = (start, end)
    # print(f"Processing range: {merged_range}, sorted_starts left: {sorted_starts}")
    while sorted_starts:
        next_start, next_end = sorted_starts[0]
        # print(f"Comparing with: {(next_start, next_end)}")
        if next_start <= merged_range[1] + 1:
            merged_range = (merged_range[0], max(next_end, merged_range[1]))
            sorted_starts.pop(0)
            # print(f"New merged range: {merged_range}, sorted_starts left: {sorted_starts}")
        else:
            # print(f"No overlap between {merged_range} and {(next_start, next_end)}")
            break
    process_ranges.append(merged_range)
    # print(f"Processed ranges so far: {process_ranges}\n")


result = 0
for p in process_ranges:
    result += p[1] - p[0] + 1

print(result)
