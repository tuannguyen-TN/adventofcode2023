def solve(engine: list[str]) -> list[int]:
    def extract_left(pos: int, line_index: int) -> int:
        temp = ''
        i = pos
        while i >= 0 and engine[line_index][i].isnumeric():
            temp += engine[line_index][i]
            i -= 1
        return int(temp[::-1])

    def extract_right(pos: int, line_index: int) -> int:
        temp = ''
        i = pos
        while i < len(
                engine[line_index]) and engine[line_index][i].isnumeric():
            temp += engine[line_index][i]
            i += 1
        return int(temp)

    def extract_mid(pos: int, line_index: int) -> int:
        temp = []
        temp.append(engine[line_index][pos])

        p1, p2 = pos - 1, pos + 1
        while (p1 >= 0 and engine[line_index][p1].isnumeric()) or (
                p2 < len(engine[line_index]) and engine[line_index][p2].isnumeric()):
            if engine[line_index][p1].isnumeric():
                temp.insert(0, engine[line_index][p1])
                p1 -= 1

            if engine[line_index][p2].isnumeric():
                temp.append(engine[line_index][p2])
                p2 += 1

        return int(''.join(temp))

    # we will start processing when encountering an "*"
    def extract_numbers(pos: int, line_index: int) -> int:
        nums = []
        part_num = 0

        # check horizontally

        # left
        if (pos - 1 >= 0 and engine[line_index][pos - 1].isnumeric()):
            number = extract_left(pos - 1, line_index)
            nums.append(number)
            part_num += 1

        # right
        if (pos + 1 < len(engine[line_index])
                and engine[line_index][pos + 1].isnumeric()):
            number = extract_right(pos + 1, line_index)
            nums.append(number)
            part_num += 1

        # check vertical
        previous_line_mid = False
        next_line_mid = False

        # previous line
        if line_index > 0:
            if engine[line_index - 1][pos].isnumeric():
                number = extract_mid(pos, line_index - 1)
                nums.append(number)
                part_num += 1
                previous_line_mid = True

        # next line
        if line_index + 1 < len(engine):
            if engine[line_index + 1][pos].isnumeric():
                number = extract_mid(pos, line_index + 1)
                nums.append(number)
                part_num += 1
                next_line_mid = True

        # check diagonal

        # previous line
        if not previous_line_mid and line_index > 0:
            # left
            if (pos - 1 >= 0 and engine[line_index - 1][pos - 1].isnumeric()):
                number = extract_left(pos - 1, line_index - 1)
                nums.append(number)
                part_num += 1

            # right
            if (pos + 1 < len(engine[line_index])
                    and engine[line_index - 1][pos + 1].isnumeric()):
                number = extract_right(pos + 1, line_index - 1)
                nums.append(number)
                part_num += 1

        # next line
        if not next_line_mid and line_index + 1 < len(engine):
            # left
            if (pos - 1 >= 0 and engine[line_index + 1][pos - 1].isnumeric()):
                number = extract_left(pos - 1, line_index + 1)
                nums.append(number)
                part_num += 1

            # right
            if (pos + 1 < len(engine[line_index])
                    and engine[line_index + 1][pos + 1].isnumeric()):
                number = extract_right(pos + 1, line_index + 1)
                nums.append(number)
                part_num += 1

        # return nums if part_num == 2 else [0, 0]
        return nums[0] * nums[1] if part_num == 2 else 0

    res = 0

    # iterating through the lines of engine
    for line_index in range(len(engine)):
        for pos in range(len(engine[line_index])):
            if engine[line_index][pos] == '*':
                output = extract_numbers(pos, line_index)
                res += output

    return res


with open('input.txt', 'r') as f:
    # with open('small.txt', 'r') as f:
    lines = f.read().split('\n')


print(solve(lines))
