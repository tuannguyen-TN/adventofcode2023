def solve(game_info: str) -> int:
    bag = {'red': 0, 'green': 0, 'blue': 0}

    game_id, game_stats = game_info.split(': ')
    game_id = game_id.split(' ')[1]

    turns = game_stats.split('; ')
    for turn in turns:
        cube_colors = turn.split(', ')
        for cube_info in cube_colors:
            num, color = cube_info.split(' ')
            bag[color] = max(bag[color], int(num))

    print(bag)
    return bag['red'] * bag['green'] * bag['blue']

# print(solve(input()))


with open('input.txt', 'r') as f:
    lines = f.read().split('\n')

total = 0

for string in lines:
    total += solve(string)

print(total)
