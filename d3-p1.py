with open ("joltages.csv", "r") as f:
    joltages = [line.strip() for line in f.readlines()]

largest_digit = '0'
largest_position = 0

second_largest_digit = '0'
total_sum = 0

for joltage in joltages:
    largest_digit = '0'
    largest_position = 0
    second_largest_digit = '0'
    for i,char in enumerate(joltage[:-1]):
        if char > largest_digit:
            largest_digit = char
            largest_position = i
   
    for j, second_char in enumerate(joltage[largest_position+1:]):
        if second_char > second_largest_digit:
            second_largest_digit = second_char

    total_sum += int(largest_digit + second_largest_digit)
    
print(f'total_sum: {total_sum}')