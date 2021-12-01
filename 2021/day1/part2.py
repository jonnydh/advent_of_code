#Given a list of numbers, delimeted by new lines
#   Read from input file and parse each item as item in list
#   create counter and indexA & indexB
#   Create two small arrays: A & B with starting vals
#   iterate through lines with while loop
#   Condition will have to be in the loop AFTER comparison, 
#   otherwise final comparison will break due to appending increased index

lines = []

with open('2021/day1/input.txt') as file:
    for line in file:
        lines.append(int(line.strip()))

count = 0
a_index = 3
b_index = 4

a = [lines[0],lines[1],lines[2]]
b = [lines[1],lines[2],lines[3]]

while True:
    if sum(b) > sum(a):
        count += 1
    if b_index == len(lines):
        break
    a.pop(0)
    a.append(lines[a_index])
    b.pop(0)
    b.append(lines[b_index]

    a_index += 1
    b_index += 1

print(count)
        