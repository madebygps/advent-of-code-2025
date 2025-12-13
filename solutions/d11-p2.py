from collections import defaultdict
from functools import lru_cache

with open('../inputs/devices.txt') as f:
    lines = f.readlines()

graph = defaultdict(tuple)

for line in lines:
    parts = line.strip().split(': ')
    source = parts[0]
    destinations = tuple(parts[1].split())
    graph[source] = destinations

@lru_cache(maxsize=None)
def count_to(target):
    if target == 'svr':
        return 1
    total = 0
    for node, neighbors in graph.items():
        if target in neighbors:
            total += count_to(node)
    return total

@lru_cache(maxsize=None)
def count_from(start):
    if start == 'out':
        return 1
    total = 0
    for neighbor in graph.get(start, ()):
        total += count_from(neighbor)
    return total

paths_to_dac = count_to('dac')
paths_to_fft = count_to('fft')
paths_from_dac = count_from('dac')
paths_from_fft = count_from('fft')

@lru_cache(maxsize=None)
def count_between(start, end):
    if start == end:
        return 1
    total = 0
    for neighbor in graph.get(start, ()):
        total += count_between(neighbor, end)
    return total

paths_dac_to_fft = count_between('dac', 'fft')
paths_fft_to_dac = count_between('fft', 'dac')

result = paths_to_dac * paths_dac_to_fft * paths_from_fft + \
         paths_to_fft * paths_fft_to_dac * paths_from_dac

print(result)
