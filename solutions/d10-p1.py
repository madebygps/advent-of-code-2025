from itertools import combinations

def solve_machine(target, buttons, num_lights):
    min_presses = float('inf')
    
    for num_buttons in range(len(buttons) + 1):
        if num_buttons >= min_presses:
            break
        for combo in combinations(range(len(buttons)), num_buttons):
            state = [0] * num_lights
            for btn_idx in combo:
                for light in buttons[btn_idx]:
                    state[light] ^= 1
            if state == target:
                min_presses = num_buttons
                break
    
    return min_presses

with open('../inputs/lights.txt') as f:
    lines = f.readlines()

total_presses = 0

for line in lines:
    diagram, *button_strs, _ = line.split()
    
    target = [1 if c == '#' else 0 for c in diagram.strip('[]')]
    num_lights = len(target)
    
    buttons = []
    for b in button_strs:
        indices = [int(x) for x in b.strip('()').split(',')]
        buttons.append(indices)
    
    min_presses = solve_machine(target, buttons, num_lights)
    total_presses += min_presses

print(total_presses)
    

    
    