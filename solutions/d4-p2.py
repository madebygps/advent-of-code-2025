with open("giftpapergrid.txt") as f:
    grid = [
        list(line.strip()) for line in f
    ] 

total_removed = 0

while True:
    
    removed_this_pass = 0
    rolls_to_remove = []

    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == "@":
                paper_neighbors = 0
                
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
                    rolls_to_remove.append((row, col))

    # Remove all accessible rolls found in this pass
    for r, c in rolls_to_remove:
        grid[r][c] = "."
        removed_this_pass += 1

    total_removed += removed_this_pass

    if removed_this_pass == 0:
        break

for row in grid:
    print("".join(row))

print("Total rolls removed:", total_removed)
