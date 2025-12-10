with open('../inputs/beams.txt') as f:
    grid = [line.rstrip() for line in f]

beams = set()

splitters = set()

split_counter =0

for row in grid:
    for col_index, item in enumerate(row):
        if item == 'S':
            beams.add(col_index)

for row in grid:
    new_beams = set()
    beams_to_remove = set()

    for col_index, char in enumerate(row):
        if char == '^' and col_index in beams:
            split_counter += 1
            beams_to_remove.add(col_index)
            new_beams.add(col_index+1)
            new_beams.add(col_index-1)
    beams.difference_update(beams_to_remove)
    beams.update(new_beams)

print(beams)
print(split_counter)



