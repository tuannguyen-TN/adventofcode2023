bag = {'red': 12, 'green': 13, 'blue': 14}

def solve(game_info: str) -> int:
    game_id, game_stats = game_info.split(': ')
    game_id = game_id.split(' ')[1]

    turns = game_stats.split('; ')
    for turn in turns:
        cube_colors = turn.split(', ')
        for cube_info in cube_colors:
            num, color = cube_info.split(' ')
            if int(num) > bag[color]:
                return 0

    return int(game_id)

# print(solve(input()))

with open('input.txt', 'r') as f:
    lines = f.read().split('\n')

total = 0

for string in lines:
    total += solve(string)

print(total)