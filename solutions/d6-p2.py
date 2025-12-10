with open('../inputs/worksheet.txt') as f:
    grid = [line.rstrip() for line in f] 


max_width = max(len(line) for line in grid)
grid = [line.ljust(max_width) for line in grid]


transposed = [list(row) for row in zip(*grid)]


transposed = transposed[::-1]


problems = []
current_problem = []

for col in transposed:
    if all(c == ' ' for c in col):
        if current_problem:
            problems.append(current_problem)
            current_problem = []
    else:
        current_problem.append(col)

if current_problem:
    problems.append(current_problem)

grand_total = 0

for problem in problems:
    operator = None
    for col in problem:
        if col[-1] in '+*':
            operator = col[-1]
            break
    
 
    numbers = []
    for col in problem:
     
        num_str = ''.join(c for c in col[:-1] if c != ' ')
        if num_str:
            numbers.append(int(num_str))
    
    if numbers and operator:
        expression = f' {operator} '.join(str(n) for n in numbers)
        result = eval(expression)
        print(f'{expression} = {result}')
        grand_total += result

print(f'Grand total: {grand_total}')



