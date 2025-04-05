import re

with open('input.txt', 'r') as f:
    data = f.read()

pattern = r'do\(\)|don\'t\(\)|mul\(([0-9]{1,3}),([0-9]{1,3})\)'
matches = re.finditer(pattern, data)

proceed = True
total = 0
for match in matches:
    instruction = match[0]
    match instruction:
        case 'do()':
            proceed = True
        case 'don\'t()':
            proceed = False
        case _:
            if proceed:
                total += int(match[1]) * int(match[2])

print(total)

