
left_list = []
right_list = []

# put them in the left and right lists appropriately
with open('input.txt', 'r') as f:
    for line in f:
        left_int, right_int = map(int, line.split())
        left_list.append(left_int)
        right_list.append(right_int)
        
# sort both lists
sorted_left_list = sorted(left_list)
sorted_right_list = sorted(right_list)

# find the difference and save that
sum_of_differences = 0

for i in range(len(left_list)):
    sum_of_differences += abs(sorted_left_list[i] - sorted_right_list[i])


print(sum_of_differences)

