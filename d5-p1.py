with open('food-db.txt') as f:
    sections = f.read().split('\n\n')

food_ranges = [
    tuple(map(int, r.split('-'))) 
    for r in sections[0].strip().split('\n')
]
food_ids = [int(id) for id in sections[1].strip().split('\n')]

ids_in_range_count = 0

for id_num in food_ids:
    for lower, upper in food_ranges:
        if lower <= id_num <= upper:
            ids_in_range_count += 1
            break


print(f'Number of food IDs in any range: {ids_in_range_count}')