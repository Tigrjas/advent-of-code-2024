import re, math

with open('input.txt', 'r') as f:
    data = f.read()

pattern = r'mul\(([0-9]{1,3}),([0-9]{1,3})\)'
matches = re.findall(pattern, data)
total = sum([int(a) * int(b) for a,b in matches])

print(total)

