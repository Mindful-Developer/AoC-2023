with open('in', 'r') as f:
    lines = f.readlines()

nums = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
    '0': '0',
    '1': '1',
    '2': '2',
    '3': '3',
    '4': '4',
    '5': '5',
    '6': '6',
    '7': '7',
    '8': '8',
    '9': '9'
}

# Part 1
print(sum([int((y := [x for x in line if x.isnumeric()])[0] + y[-1]) for line in lines]))

total = 0
# Part 2
for line in lines:
    line_nums = []

    for i in range(len(line)):
        for j in range(1, 6):
            if i + j > len(line):
                break
            if (x := line[i:i+j]) in nums:
                line_nums.append(nums[x])
                break
    total += int(''.join(line_nums[0] + line_nums[-1]))

print(total)
