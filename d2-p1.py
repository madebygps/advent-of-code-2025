with open("ranges.csv", "r") as f:
    ranges = f.read().strip().split(',')

total_sum = 0

for r in ranges:
    # could use split, but map splits and converts to int in one go
    start, end = map(int, r.split('-'))
    for i in range(start, end + 1):
        s = str(i)
        if len(s) % 2 == 0:
            mid_point = len(s) // 2
            first_half, second_half = s[:mid_point], s[mid_point:]
            if first_half == second_half:
                total_sum += i

print(f"Total matching numbers found: {total_sum}")