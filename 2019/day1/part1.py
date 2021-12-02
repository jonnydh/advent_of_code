inputs = []

with open('input.txt') as file:
    for line in file:
        inputs.append(int(line.strip()))

def floor_divide_by_three(num):
    return num // 3

def subtract_two(num):
    return num - 2

def calculate_module_fuel(num):
    return subtract_two(floor_divide_by_three(num))

##Part1
output = 0
for num in inputs:
    output += calculate_module_fuel(num)
print(output)

def calculate_fuel_for_fuel(num):
    total_module_fuel = 0
    while calculate_module_fuel(num) > 0:
        num = calculate_module_fuel(num)
        total_module_fuel += num
    return total_module_fuel

#Part2
output = 0
for num in inputs:
    output += calculate_fuel_for_fuel(num)
print(output)