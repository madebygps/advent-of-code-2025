with open ("joltages.csv", "r") as f:
    joltages = [line.strip() for line in f.readlines()]


total_sum = 0

for joltage in joltages:
    result = ''
    position = 0
    for digits_needed in range(12, 0, -1):
        
        max_index = len(joltage) - digits_needed
        largest_digit = '0'
        largest_position = position

        for i in range(position, max_index+1):
            if joltage[i] > largest_digit:
                largest_digit = joltage[i]
                largest_position = i
        result += largest_digit
        position = largest_position + 1
    
    print(f'joltage: {joltage}, result: {result}')
    total_sum += int(result)
    print(f'total_sum so far: {total_sum}')