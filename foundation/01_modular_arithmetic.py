"""
Foundation 1: Modular Arithmetic
================================
PATTERN: Wrap-around / cycles / circular → use MODULO (%)

Rule: anything % n gives a number in range [0, n-1]
"""

# =============================================================================
# PART 1: Basic Modulo - Where do you land?
# =============================================================================

DIAL_SIZE = 100  # Dial has positions 0-99

def move_forward(position, steps):
    """Move clockwise on the dial."""
    return (position + steps) % DIAL_SIZE

def move_backward(position, steps):
    """Move counter-clockwise on the dial."""
    return (position - steps) % DIAL_SIZE

# Try it:
print("=== Basic Movement ===")
print(f"Start at 95, move forward 10: {move_forward(95, 10)}")   # expect 5
print(f"Start at 5, move backward 10: {move_backward(5, 10)}")   # expect 95


# =============================================================================
# EXERCISE 1: Clock Math
# =============================================================================
# A clock has positions 0-11 (like hours, but 0-indexed)
# Complete the function:

CLOCK_SIZE = 12

def what_hour(start_hour, hours_later):
    """Given a starting hour (0-11), what hour is it after hours_later?"""
    return(start_hour+hours_later) % CLOCK_SIZE

# Test your solution:
print(f"3 hours after 10: {what_hour(10, 3)}")  # expect 1
print(f"25 hours after 5: {what_hour(5, 25)}")  # expect 6


# =============================================================================
# EXERCISE 2: Circular Array Access
# =============================================================================
# Access elements from a list as if it wraps around forever

def circular_get(lst, index):
    """Get element at index, wrapping around if index >= len(lst)."""
    if index >= len(lst):
        index = index % len(lst)
    return lst[index]

# Test your solution:
colors = ['red', 'green', 'blue']
print(f"Index 0: {circular_get(colors, 0)}")   # expect 'red'
print(f"Index 3: {circular_get(colors, 3)}")   # expect 'red' (wrapped!)
print(f"Index 7: {circular_get(colors, 7)}")   # expect 'green'


# =============================================================================
# PART 2: Counting Boundary Crossings (Day 1 needs this!)
# =============================================================================
# Problem: How many times do we cross position 0?

def count_zero_crossings_right(position, steps):
    """Count times we cross 0 moving RIGHT (increasing)."""
    dist_to_zero = DIAL_SIZE - position  # steps until we hit 0
    
    if steps < dist_to_zero:
        return 0
    
    remaining = steps - dist_to_zero
    return 1 + (remaining // DIAL_SIZE)

def count_zero_crossings_left(position, steps):
    """Count times we cross 0 moving LEFT (decreasing)."""
    dist_to_zero = position if position > 0 else DIAL_SIZE
    
    if steps < dist_to_zero:
        return 0
    
    remaining = steps - dist_to_zero
    return 1 + (remaining // DIAL_SIZE)

# Try it:
print("\n=== Boundary Crossings ===")
print(f"From 95, go right 250: {count_zero_crossings_right(95, 250)} crossings")  # expect 3


# =============================================================================
# EXERCISE 3: Count crossings of ANY boundary
# =============================================================================
# Generalize: count how many times we cross a specific position (not just 0)

def count_crossings(start, steps, boundary, dial_size, direction='right'):
    """
    Count how many times we cross 'boundary' moving in 'direction'.
    
    Hint: Shift coordinates so boundary becomes 0, then use the logic above.
    """

    shifted_start = (start - boundary) % dial_size
    distance_to_zero = dial_size - shifted_start
    
    if steps < distance_to_zero:
        return 0
    
    remaining = steps - distance_to_zero
    return 1 + (remaining // dial_size)



# Test your solution:
print(f"From 30, go right 150, cross 50: {count_crossings(30, 150, 50, 100, 'right')}")  # expect 2


# =============================================================================
# EXERCISE 4: Process multiple instructions
# =============================================================================
# Given a list of (direction, steps) tuples, track position AND total crossings

def process_instructions(instructions, start_pos=0):
    """
    Process list of ('L', steps) or ('R', steps) instructions.
    Return (final_position, total_zero_crossings)
    """
    position = start_pos
    crossings = 0
    
    for direction, steps in instructions:
        # TODO: Update position and count crossings
        pass
    
    return position, crossings

# Test your solution:
# test_instructions = [('R', 30), ('L', 10), ('R', 150)]
# pos, crosses = process_instructions(test_instructions)
# print(f"Final position: {pos}, Zero crossings: {crosses}")
