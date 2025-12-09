

with open('tiles.txt') as f:
    tiles = f.readlines()

max_area = 0

for i, tile in enumerate(tiles):
    x1, y1 = tile.strip().split(',')
    for tile2 in tiles[i+1:]:
        x2, y2 = tile2.strip().split(',')
        if x2 != x1 and y1 != y2:
            area = (abs(int(x2)-int(x1)) + 1) * (abs(int(y2) - int(y1)) + 1)
            print(area)
            if area > max_area:
                max_area = area

print(max_area)