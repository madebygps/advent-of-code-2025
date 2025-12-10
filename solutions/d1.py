DIAL_SIZE = 100
current_position = 50
total_zeros = 0

with open("instructions.csv", "r") as f:
    instructions = f.read().strip().split()

for instruction in instructions:
    direction = instruction[0]
    amount = int(instruction[1:])


    # We have to add
    if direction == "R":
        dist_to_zero = DIAL_SIZE - current_position

        # If we cross zero
        if amount >= dist_to_zero:
            # Count how many times we cross zero, including if we land on it
            remaining_distance = amount - dist_to_zero
            additional_loops = remaining_distance // DIAL_SIZE
            total_zeros += 1 + additional_loops

        # move the current position forward taking wrap-around into account
        current_position = (current_position + amount) % DIAL_SIZE

    # We have to subtract
    elif direction == "L":
        # if we are at zero, distance is full dial size
        dist_to_zero = current_position if current_position > 0 else DIAL_SIZE

        if amount >= dist_to_zero:
            remaining_distance = amount - dist_to_zero
            additional_loops = remaining_distance // DIAL_SIZE
            total_zeros += 1 + additional_loops
        # move the current position backward taking wrap-around into account
        current_position = (current_position - amount) % DIAL_SIZE

print(f"Password: {total_zeros}")
