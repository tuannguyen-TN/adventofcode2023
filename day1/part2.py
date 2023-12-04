def solve(string):
    if len(string.strip()) == 0:
        return 0

    mappings = {
        'zero':0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9
    }

    index_num_pairs = {}

    left, right = 0, 0
    temp = ''

    while left < len(string):
        if right >= len(string):
            left += 1
            right = left - 1
            temp = ''

        if string[right].isnumeric():
            index_num_pairs[right] = int(string[right])

        temp += string[right]
        # print(temp)

        if temp in mappings:
            index_num_pairs[left] = int(mappings[temp])

        if len(temp) >= 5 or right >= len(string):
            left += 1
            right = left - 1
            temp = ''

        right += 1

    print(index_num_pairs)
    first_digit = index_num_pairs[min(list(index_num_pairs.keys()))]
    last_digit = index_num_pairs[max(list(index_num_pairs.keys()))]
    return first_digit * 10 + last_digit

# print(solve('xktoneighttwoqljrsctbzxxqjtwo1ftsjczrsevenzqcdxtnktwo'))

with open('input.txt', 'r') as f:
    lines = f.read()

total = 0

for string in lines.split('\n'):
    # solve(string)
    total += solve(string)

print(total)
