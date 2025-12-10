import bisect

with open('../inputs/tiles.txt') as f:
    tiles = [tuple(map(int, line.strip().split(','))) for line in f.readlines()]

# Build edges as horizontal/vertical segments
def get_edges(tiles):
    """Get all edges as (horizontal, vertical) lists of segments"""
    n = len(tiles)
    h_edges = []  # (y, x_min, x_max)
    v_edges = []  # (x, y_min, y_max)
    
    for i in range(n):
        x1, y1 = tiles[i]
        x2, y2 = tiles[(i + 1) % n]
        
        if x1 == x2:  # vertical
            v_edges.append((x1, min(y1, y2), max(y1, y2)))
        else:  # horizontal
            h_edges.append((y1, min(x1, x2), max(x1, x2)))
    
    return h_edges, v_edges

def get_valid_x_ranges_for_row(y, v_edges, h_edges_by_y):
    """For a given row y, return list of (x_min, x_max) ranges that are valid"""
    crossings = []
    for x, y_min, y_max in v_edges:
        if y_min < y < y_max:
            crossings.append(x)
        elif y == y_min:
            crossings.append(x)
    
    h_on_row = h_edges_by_y.get(y, [])
    crossings.sort()
    
    ranges = []
    for i in range(0, len(crossings) - 1, 2):
        ranges.append((crossings[i], crossings[i + 1]))
    
    all_ranges = ranges + h_on_row
    if not all_ranges:
        return []
    
    all_ranges.sort()
    merged = [all_ranges[0]]
    for r_min, r_max in all_ranges[1:]:
        if r_min <= merged[-1][1] + 1:
            merged[-1] = (merged[-1][0], max(merged[-1][1], r_max))
        else:
            merged.append((r_min, r_max))
    
    return merged

h_edges, v_edges = get_edges(tiles)

# Build h_edges_by_y
h_edges_by_y = {}
for y, x_min, x_max in h_edges:
    if y not in h_edges_by_y:
        h_edges_by_y[y] = []
    h_edges_by_y[y].append((x_min, x_max))

# Get all critical y values (where the row ranges change)
critical_ys = set()
for y, _, _ in h_edges:
    critical_ys.add(y)
for x, y_min, y_max in v_edges:
    critical_ys.add(y_min)
    critical_ys.add(y_max)
critical_ys = sorted(critical_ys)

# Pre-compute ranges only at critical y values and in-between
# The ranges between two consecutive critical ys are constant!
print("Pre-computing row ranges at critical points...")
row_at_y = {}

# Compute ranges at each critical y
for y in critical_ys:
    row_at_y[y] = get_valid_x_ranges_for_row(y, v_edges, h_edges_by_y)

# Also compute for a sample y in each interval (ranges are constant there)
intervals = []
for i in range(len(critical_ys) - 1):
    y_lo = critical_ys[i]
    y_hi = critical_ys[i + 1]
    if y_hi > y_lo + 1:
        mid_y = y_lo + 1  # Sample one row in between
        row_at_y[mid_y] = get_valid_x_ranges_for_row(mid_y, v_edges, h_edges_by_y)
        intervals.append((y_lo + 1, y_hi - 1, mid_y))  # (start, end, sample_y)

def get_ranges_for_y(y):
    """Get ranges for y using cached values"""
    if y in row_at_y:
        return row_at_y[y]
    # Find which interval y is in - ranges there are same as sample
    for y_lo, y_hi, sample_y in intervals:
        if y_lo <= y <= y_hi:
            return row_at_y[sample_y]
    return []

# Build a more efficient structure: for each critical y, store the ranges
# Then we can binary search intervals


def check_rectangle_valid_fast(x_min, x_max, y_min, y_max):
    """Check if entire rectangle is within valid area using critical y values"""
    # The key insight: ranges only change at critical_ys
    # So we only need to check:
    # 1. All critical y values within [y_min, y_max]
    # 2. One sample point from each interval between critical ys that overlaps [y_min, y_max]
    
    # Find which critical ys are in our range
    lo = bisect.bisect_left(critical_ys, y_min)
    hi = bisect.bisect_right(critical_ys, y_max)
    
    # Collect all y values we need to check
    ys_to_check = set()
    
    # Add all critical ys in range
    for i in range(lo, hi):
        ys_to_check.add(critical_ys[i])
    
    # Add sample points from intervals
    # If y_min is before the first critical y in range, check y_min
    if lo == 0 or critical_ys[lo - 1] < y_min:
        ys_to_check.add(y_min)
    if hi == len(critical_ys) or critical_ys[hi - 1] < y_max:
        ys_to_check.add(y_max)
    
    # Add interval midpoints
    relevant_crits = [y_min] + critical_ys[lo:hi] + [y_max]
    for i in range(len(relevant_crits) - 1):
        y1, y2 = relevant_crits[i], relevant_crits[i + 1]
        if y2 > y1:
            ys_to_check.add(y1)
            if y2 > y1 + 1:
                ys_to_check.add(y1 + 1)  # Sample in interval
    
    # Check each y value
    for y in ys_to_check:
        if y < y_min or y > y_max:
            continue
        ranges = get_ranges_for_y(y)
        if not any(r_min <= x_min and r_max >= x_max for r_min, r_max in ranges):
            return False
    
    return True

print("Searching for best rectangle...")

# Group tiles by y
tiles_by_y = {}
for x, y in tiles:
    if y not in tiles_by_y:
        tiles_by_y[y] = []
    tiles_by_y[y].append(x)

for y in tiles_by_y:
    tiles_by_y[y].sort()

ys = sorted(tiles_by_y.keys())

max_area = 0
total_pairs = sum(len(tiles_by_y[y1]) * len(tiles_by_y[y2]) 
                   for i, y1 in enumerate(ys) for y2 in ys[i+1:])
print(f"Total pairs to check: {total_pairs}")

checked = 0
for i, y1 in enumerate(ys):
    for y2 in ys[i+1:]:
        height = y2 - y1 + 1
        xs1 = tiles_by_y[y1]
        xs2 = tiles_by_y[y2]
        
        for x1 in xs1:
            for x2 in xs2:
                checked += 1
                if checked % 100000 == 0:
                    print(f"Checked {checked}/{total_pairs}, best so far: {max_area}")
                
                if x1 == x2:
                    continue
                    
                min_x, max_x = min(x1, x2), max(x1, x2)
                width = max_x - min_x + 1
                area = width * height
                
                if area <= max_area:
                    continue
                
                if check_rectangle_valid_fast(min_x, max_x, y1, y2):
                    max_area = area
                    print(f"New best: {max_area} at ({min_x},{y1})-({max_x},{y2})")

print(max_area)