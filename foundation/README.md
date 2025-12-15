# 🎄 Advent of Code - Algorithmic Foundations

Reverse-engineering Day 1 into the concepts, patterns, and algorithmic thinking behind the solution.

## 📚 Concepts (Day 1)

| # | File | Concept |
|---|------|---------|
| 1 | [01_modular_arithmetic.py](01_modular_arithmetic.py) | Circular structures, wrap-around math, boundary crossing formulas |
| 2 | [02_simulation_vs_closedform.py](02_simulation_vs_closedform.py) | When to simulate step-by-step vs. compute directly |
| 3 | [03_state_machines.py](03_state_machines.py) | Minimal state, state transitions, tracking patterns |
| 4 | [04_problem_decomposition.py](04_problem_decomposition.py) | Breaking problems into independent sub-problems |
| 5 | [05_problem_types.py](05_problem_types.py) | Recognizing AoC archetypes: simulation, search, DP, graphs, etc. |
| 6 | [06_complexity.py](06_complexity.py) | Complexity analysis, when/how to optimize |
| 7 | [07_day1_annotated.py](07_day1_annotated.py) | Full solution with algorithmic annotations |

## 🧠 Day 1 Key Insights

**Problem type:** Simulation + Modular Arithmetic

**The naive trap:** Simulate every step → O(n × step_size)

**The insight:** Calculate crossings mathematically → O(n)

```
crossings = 1 + (steps - dist_to_boundary) // cycle_length
```

**Pattern recognition:**
- Circular structure → modulo
- "Count how many times X happens" → find formula instead of counting
- Large step values → MUST use math, not iteration

## 🎯 How to Use

Each file focuses on ONE concept with:
- The theoretical foundation
- How it applies to Day 1
- When you'll see this pattern again
- Exercises to test understanding

## 🔮 Expanding This

As you work through more days, we can add:
- `foundation-d2/` - concepts from Day 2
- Common patterns that span multiple days
- Data structure foundations (graphs, trees, heaps)
