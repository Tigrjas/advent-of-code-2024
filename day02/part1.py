
def is_safe(numbers):
    safety = True
    direction = None
    
    # Set the direction
    if numbers[0] - numbers[1] < 1:
        direction = "decreasing"
    else:
        direction = "increasing"

    for i in range(len(numbers)):
        if i == len(numbers) - 1: # break before reaching end
            break
        difference = numbers[i] - numbers[i+1]
        if difference == 0: # check for no change
            return False
        if difference < 1: # check for decreasing
            if direction != "decreasing":
                return False
        else: # check for true
            if direction != "increasing":
                return False

        # check if change is between 1-3
        if abs(difference) not in range(1, 4):
            return False
    
    return True

safe_levels = 0

with open('input.txt', 'r') as f:
    for line in f:
        levels = list(map(int, line.split()))
        if is_safe(levels):
            safe_levels += 1

print(f"Number of safe reports: {safe_levels}")
        
        