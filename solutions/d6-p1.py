with open('../inputs/worksheet.txt') as f:
    grid = [list(line.strip().split()) for line in f]

transposed = [list(row) for row in zip(*grid)]

sum = 0

for exercise in transposed:
    result = 0
    exercise_total = 0
    
    total_operands = len(exercise) - 1
    exercise_string = ''

    for i in range(total_operands):
            exercise_string += exercise[i]
            if i < total_operands - 1:
                exercise_string += ' '
                exercise_string += exercise[-1]
                exercise_string += ' '
    exercise_total = eval(exercise_string)
    
    print(exercise_total)
    sum += exercise_total

print(f'Sum of all results: {sum}')



