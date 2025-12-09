import math

with open('boxes.txt') as f:
    boxes = [tuple(map(int, line.split(','))) for line in f]

pairs = []

for i, box in enumerate(boxes):
    for j in range(i+1, len(boxes)):
            pairs.append((boxes[i], boxes[j]))

pairs_and_distances = []

for pair in pairs:

    coordinates1, coordinates2 = pair
    x1, y1, z1 = coordinates1
    x2, y2, z2 = coordinates2
    
    # sqrt((x₂-x₁)² + (y₂-y₁)² + (z₂-z₁)²)

    distance = math.sqrt(math.pow(x2 - x1, 2) 
                         + math.pow(y2 - y1, 2) 
                         + math.pow(z2-z1, 2))
    
    pair_and_distance = (distance, pair)
    
    pairs_and_distances.append(pair_and_distance)


pairs_and_distances.sort()

parent = {}

for box in boxes:
     parent[box] = box

def find_parent(box):
    while parent[box] != box:
          box = parent[box]
    return box

num_circuits = len(boxes)

for distance, (box1, box2) in pairs_and_distances:
    root1 = find_parent(box1)
    root2 = find_parent(box2)
    
    if root1 != root2:
         parent[root1] = root2
         num_circuits -= 1
         
         if num_circuits == 1:
             print(f"Last connection between {box1} and {box2}")
             print(f"Answer: {box1[0] * box2[0]}")
             break
