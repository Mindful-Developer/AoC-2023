from string import punctuation
from collections import defaultdict


punctuation = punctuation.replace('.', '')

with open('in', 'r') as f:
    lines = f.readlines()

LINE_LEN = len(lines[0].strip())


def is_symbol_neighbour(segment_start: (int, int), segment_end: (int, int)):
    """checks if the segment has a neighbour symbol adjacent (including diagonally)"""
    for i in range(segment_start[0] - 1, segment_end[0] + 2):
        for j in range(segment_start[1] - 1, segment_end[1] + 1):
            if i < 0 or j < 0 or i >= len(lines) or j >= LINE_LEN:
                continue
            if lines[i][j] in punctuation:
                return True
    return False


# part 1
total = 0
for i, line in enumerate(lines):
    segment_start = None
    for j, col in enumerate(line.strip()):
        if col.isdigit():
            if segment_start is None:
                segment_start = (i, j)
        else:
            if segment_start is not None:
                if is_symbol_neighbour(segment_start, (i, j)):
                    total += int(line[segment_start[1]:j])
                segment_start = None
    else:
        if segment_start is not None:
            if is_symbol_neighbour(segment_start, (i, j)):
                total += int(line[segment_start[1]:j+1])
            segment_start = None
print(total)


# part 2
GEAR = '*'
total = 0
gears = []


def get_symbol_neighbour_gears(segment_start, segment_end):
    """checks if the segment has a neighbour symbol adjacent (including diagonally)"""
    for i in range(segment_start[0] - 1, segment_end[0] + 2):
        for j in range(segment_start[1] - 1, segment_end[1] + 1):
            if i < 0 or j < 0 or i >= len(lines) or j >= LINE_LEN:
                continue
            if lines[i][j] == GEAR:
                gears.append(((i, j), int(lines[segment_start[0]][segment_start[1]:segment_end[1]])))


for i, line in enumerate(lines):
    segment_start = None
    for j, col in enumerate(line.strip()):
        if col.isdigit():
            if segment_start is None:
                segment_start = (i, j)
        else:
            if segment_start is not None:
                get_symbol_neighbour_gears(segment_start, (i, j))
                segment_start = None
    else:
        if segment_start is not None:
            get_symbol_neighbour_gears(segment_start, (i, j + 1))
            segment_start = None

gear_dict = defaultdict(list)
for gear in gears:
    gear_dict[gear[0]].append(gear[1])

total2 = 0
# if the gear has two items in the list, multiply them and add to total
for gear in gear_dict:
    if len(gear_dict.get(gear)) == 2:
        total2 += gear_dict.get(gear)[0] * gear_dict.get(gear)[1]

print(total2)