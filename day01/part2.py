from collections import Counter

left_list = []
right_list = []

# put them in the left and right lists appropriately
with open('input.txt', 'r') as f:
    for line in f:
        left_int, right_int = map(int, line.split())
        left_list.append(left_int)
        right_list.append(right_int)

right_list_count = Counter(right_list)

similarity_score = 0 # number in left list multiplied by occurances in right list

for i in range(len(left_list)):
    similarity_score += left_list[i] * right_list_count[left_list[i]]

print(similarity_score)
