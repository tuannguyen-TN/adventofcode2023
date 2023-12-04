def solve(string):
    if len(string.strip()) == 0:
        return 0

    p1, p2 = 0, len(string) - 1

    while not (string[p1].isnumeric()):
        p1 += 1

    while not (string[p2].isnumeric()):
        p2 -= 1

    return int(string[p1]) * 10 + int(string[p2])


with open('input.txt', 'r') as f:
    lines = f.read()

total = 0

for string in lines.split('\n'):
    total += solve(string)

print(total)
