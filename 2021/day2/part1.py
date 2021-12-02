input_as_list = []

with open('2021/day2/input.txt') as file:
    for line in file:
        input_as_list.append(line.strip().split())


depth = 0
horizontal = 0

for command in input_as_list:
    if command[0] == 'forward':
        horizontal += int(command[1])
    elif command[0] == 'up':
        depth -= int(command[1])
    else: 
        depth += int(command[1])

print(depth * horizontal)
