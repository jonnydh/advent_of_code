#Plan

#Given a list of numbers, delimeted by new lines
#   Read from input file and parse each item as item in list
#   create counter
#   increment counter if number is bigger than prev number
#   omit first check as no previous number

lines = []

with open('2021/day1/input.txt') as file:
    for line in file:
        lines.append(int(line.strip()))

count = 0
index = 1

while index < len(lines):
    if lines[index] > lines[index-1]:
        count += 1
    index += 1

print(count)
        
