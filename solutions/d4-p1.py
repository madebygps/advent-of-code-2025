with open("giftpapergrid.txt") as f:
    grid = [
        list(line.strip()) for line in f
    ]  
new_grid = [row.copy() for row in grid] 
accessible_rolls = 0

for row in range(len(grid)):
    for col in range(len(grid[row])):
        paper_neighbors = 0
        if grid[row][col] == "@":
            # Check immediate right neighbor
            if col + 1 < len(grid[row]) and grid[row][col + 1] == "@":
                paper_neighbors += 1

            # Check immediate left neighbor
            if col - 1 >= 0 and grid[row][col - 1] == "@":
                paper_neighbors += 1

            # Check immediate bottom neighbor
            if row + 1 < len(grid) and grid[row + 1][col] == "@":
                paper_neighbors += 1

            # Check immediate bottom-right neighbor
            if row + 1 < len(grid) and col + 1 < len(grid[row]) and grid[row + 1][col + 1] == "@":
                paper_neighbors += 1

            # Check immediate bottom-left neighbor
            if row + 1 < len(grid) and col - 1 >= 0 and grid[row + 1][col - 1] == "@":
                paper_neighbors += 1

            # Check immediate top neighbor
            if row - 1 >= 0 and grid[row - 1][col] == "@":
                paper_neighbors += 1

            # Check immediate top-right neighbor
            if row - 1 >= 0 and col + 1 < len(grid[row]) and grid[row - 1][col + 1] == "@":
                paper_neighbors += 1

            # Check immediate top-left neighbor
            if row - 1 >= 0 and col - 1 >= 0 and grid[row - 1][col - 1] == "@":
                paper_neighbors += 1

            if paper_neighbors < 4:
                new_grid[row][col] = "X"
                accessible_rolls += 1


for row in new_grid:
    print("".join(row))

print("Accessible rolls:", accessible_rolls)
