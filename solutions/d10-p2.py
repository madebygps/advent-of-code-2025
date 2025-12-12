from scipy.optimize import milp, LinearConstraint, Bounds
import numpy as np

def solve_machine(target, buttons, num_counters):
    num_buttons = len(buttons)
    
    A = np.zeros((num_counters, num_buttons))
    for i, button in enumerate(buttons):
        for counter_idx in button:
            if counter_idx < num_counters:
                A[counter_idx][i] = 1
    
    c = np.ones(num_buttons)
    
    constraints = LinearConstraint(A, target, target)
    integrality = np.ones(num_buttons)
    bounds = Bounds(lb=0, ub=np.inf)
    
    result = milp(c, constraints=constraints, integrality=integrality, bounds=bounds)
    
    if result.success:
        return int(round(result.fun))
    else:
        return float('inf')

with open('../inputs/lights.txt') as f:
    lines = f.readlines()

total_presses = 0

for line in lines:
    diagram, *button_strs, joltage_str = line.split()
    
    target = [int(x) for x in joltage_str.strip('{}').split(',')]
    num_counters = len(target)
    
    buttons = []
    for b in button_strs:
        indices = [int(x) for x in b.strip('()').split(',')]
        buttons.append(indices)
    
    min_presses = solve_machine(target, buttons, num_counters)
    total_presses += min_presses

print(total_presses)
