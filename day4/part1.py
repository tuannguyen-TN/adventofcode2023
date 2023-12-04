def solve(card: str) -> int:
    _, numbers = card.split(': ')
    nums1, nums2 = numbers.split(' | ')

    winning_numbers = set()
    for char in nums1.split(' '):
        if char.isnumeric():
            winning_numbers.add(int(char))

    owned_numbers = set()
    for char in nums2.split(' '):
        if char.isnumeric():
            owned_numbers.add(int(char))

    matches = winning_numbers.intersection(owned_numbers)
    print('matches:', len(matches))

    return int(2 ** (len(matches) - 1))

with open('input.txt', 'r') as f:
# with open('small.txt', 'r') as f:
    lines = f.read().split('\n')

total = 0

for string in lines:
    total += solve(string)

print(total)