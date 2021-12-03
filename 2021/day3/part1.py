report = []
with open('input.txt') as file:
    for line in file:
        report.append(line.strip())

#Given a list of strings, and a position, find the most common value in that list. 

def most_common_value_at_pos(report, position):
    report_length = len(report)
    zeros = len([line[position] for line in report if line[position] == '0'])
    ones = report_length - zeros 

    if zeros > ones:
        return '0'
    elif ones > zeros:
        return '1'
    else: 
        return 'tie'

def calcualate_gamma(report):
    gamma = ''
    for pos in range(len(report[0])):
        gamma += most_common_value_at_pos(report, pos)
    return gamma

def calculate_epsilon(report):
    epsilon = ''
    for pos in range(len(report[0])):
        if most_common_value_at_pos(report,pos) == '1':
            epsilon += '0'
        else:
            epsilon += '1'
    return epsilon
    
def convert_binary_to_decimal(number):
    num_to_add = 1
    conversion = 0
    for char in number[::-1]:
        if char == '1':
            conversion += num_to_add
        num_to_add *= 2
    return conversion

def main():
    return convert_binary_to_decimal(calcualate_gamma(report)) * convert_binary_to_decimal(calculate_epsilon(report))


print(main())