with open('in', 'r') as f:
    lines = f.readlines()

RED = 12
GREEN = 13
BLUE = 14

total = 0
for line in lines:
    game_number = int(line.split('Game ')[1].split(':')[0])

    games = line.split(':')[1].split(';')
    for game in games:
        game = game.strip()
        flag = False

        for dice in game.split(','):
            dice = dice.strip()

            number = dice.split(' ')[0]
            colour = dice.split(' ')[1]

            if colour == 'red':
                if int(number) > RED:
                    flag = True
                    break
            elif colour == 'green':
                if int(number) > GREEN:
                    flag = True
                    break
            else:
                if int(number) > BLUE:
                    flag = True
                    break
        if flag:
            break
    else:
        total += game_number

print(total)


# Part 2
total2 = 0
for line in lines:
    dice_counts = {'red': 0, 'green': 0, 'blue': 0}
    game_number = int(line.split('Game ')[1].split(':')[0])

    games = line.split(':')[1].split(';')
    for game in games:
        game = game.strip()

        for dice in game.split(','):
            dice = dice.strip()

            number = dice.split(' ')[0]
            colour = dice.split(' ')[1]

            if colour == 'red':
                dice_counts['red'] = max(dice_counts['red'], int(number))
            elif colour == 'green':
                dice_counts['green'] = max(dice_counts['green'], int(number))
            else:
                dice_counts['blue'] = max(dice_counts['blue'], int(number))

    total2 += dice_counts['red'] * dice_counts['green'] * dice_counts['blue']
print(total2)
