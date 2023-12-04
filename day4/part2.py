def solve(collection: list[str]) -> int:

    def scratch_card(numbers: str) -> int:
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
        return len(matches)

    total_scratchpads = 0
    memo = {}
    copies = {}

    for card in collection:
        card_header, numbers = card.split(': ')
        card_id = int(card_header.split(' ')[-1])

        if card_id not in copies:
            copies[card_id] = 0
        copies[card_id] += 1

        memo[card_id] = scratch_card(numbers)

        for next_card_id in range(card_id + 1, card_id + 1 + memo[card_id]):
            if next_card_id not in copies:
                copies[next_card_id] = 0
            copies[next_card_id] += copies[card_id]

    return sum(copies.values())

with open('input.txt', 'r') as f:
# with open('small.txt', 'r') as f:
    lines = f.read().split('\n')

print(solve(lines))