with open('../inputs/food-db.txt') as f:
    sections = f.read().split('\n\n')

food_ranges_section = sections[0].strip().split('\n')

formatted_ranges = []
for food_range in food_ranges_section:
    lower, upper = map(int, food_range.split('-'))
    formatted_ranges.append((lower, upper))

formatted_ranges.sort()

merged_ranges = []

for current_range in formatted_ranges:
    current_lower, current_upper = current_range[0], current_range[1]
    if merged_ranges and current_lower <= merged_ranges[-1][1] + 1:
        merged_ranges[-1] = (merged_ranges[-1][0], max(merged_ranges[-1][1], current_upper))
    else:
        merged_ranges.append(current_range)


print(f'total unique ids: {sum(upper - lower + 1 for lower, upper in merged_ranges)}')