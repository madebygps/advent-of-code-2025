with open('test-beams.txt') as f:
    grid = [line.rstrip() for line in f]


from collections import Counter

beams = Counter()

for row in grid:
    for col_index, item in enumerate(row):
        if item == 'S':
            beams[col_index] += 1

for row in grid:
    new_beams = Counter()
    for col_index, char in enumerate(row):
        if col_index in beams:
            count = beams[col_index]
            if char == '^':
                new_beams[col_index+1] += count
                new_beams[col_index-1] += count
            else:
                new_beams[col_index] += count
    beams = new_beams
            

print(f'total options: {sum(beams.values())}')


