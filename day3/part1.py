def solve(engine: list[str]) -> int:
    special_characters = '`~!@#$%^&*()_-+=\\{\\}[]\\|;:"<>?,/'
    total = 0

    def extract_number(start_pos: int, line_index: int) -> (int, int):
        temp = ''
        end_pos = start_pos

        # get the numbers
        while end_pos < len(
                engine[line_index]) and engine[line_index][end_pos].isnumeric():
            temp += engine[line_index][end_pos]
            end_pos += 1

        # check symbols from left and right
        if (start_pos != 0 and engine[line_index][start_pos - 1] in special_characters) or (
                end_pos < len(engine[line_index]) and engine[line_index][end_pos] in special_characters):
            return (int(temp), end_pos - 1)

        # check symbols from previous and next lines
        if start_pos == 0:
            start = 0
        else:
            start = start_pos - 1

        for i in range(start, end_pos + 1):
            if line_index > 0:
                try:
                    if engine[line_index - 1][i] in special_characters:
                        return (int(temp), end_pos - 1)
                except BaseException:
                    continue

            if line_index < len(engine):
                try:
                    if engine[line_index + 1][i] in special_characters:
                        return (int(temp), end_pos - 1)
                except BaseException:
                    continue

        return (0, end_pos - 1)

    # iterating through the lines of engine
    for line_index in range(len(engine)):
        position = 0
        while position < len(engine[line_index]):
            if engine[line_index][position].isnumeric():
                output = extract_number(position, line_index)
                total += output[0]
                position = output[1]
            position += 1

    return total


with open('input.txt', 'r') as f:
    # with open('small.txt', 'r') as f:
    lines = f.read().split('\n')

print(solve(lines))
