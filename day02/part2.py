from typing import Tuple, Union, List

def is_safe(levels: List[int]) -> bool:
    # Check if it's strictly increasing with step between 1 and 3
    increasing = all(a < b and 1 <= b - a <= 3 for a, b in zip(levels, levels[1:]))
    # Check if it's strictly decreasing with step between 1 and 3
    decreasing = all(a > b and 1 <= a - b <= 3 for a, b in zip(levels, levels[1:]))
    return increasing or decreasing

def is_safe_with_tolerance(reports: List[str]) -> int:
    count = 0
    for report in reports:
        levels = list(map(int, report.split()))
        if is_safe(levels):
            count += 1
        else:
            # Try removing one element at a time
            for i in range(len(levels)):
                modified = levels[:i] + levels[i+1:]
                if is_safe(modified):
                    count += 1
                    break  # Only allowed to remove one level
    return count

with open('input.txt', 'r') as f:
    data = f.read().strip().splitlines()

print(f"Safe levels: {is_safe_with_tolerance(data)}")






        