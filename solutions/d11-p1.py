from collections import defaultdict

def count_paths(graph, current, target, visited):
    if current == target:
        return 1
    
    total = 0
    for neighbor in graph[current]:
        if neighbor not in visited:
            visited.add(neighbor)
            total += count_paths(graph, neighbor, target, visited)
            visited.remove(neighbor)
    
    return total

with open('../inputs/devices.txt') as f:
    lines = f.readlines()

graph = defaultdict(list)

for line in lines:
    parts = line.strip().split(': ')
    source = parts[0]
    destinations = parts[1].split()
    graph[source] = destinations

visited = {'you'}
print(count_paths(graph, 'you', 'out', visited))
