report = []
with open('input.txt') as file:
    for line in file:
        report.append(line.strip())

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

def convert_binary_to_decimal(number):
    num_to_add = 1
    conversion = 0
    for char in number[::-1]:
        if char == '1':
            conversion += num_to_add
        num_to_add *= 2
    return conversion

def oxy_generator(report):
    oxy_report = report.copy()
    for pos in range(len(oxy_report[0])):
        common = most_common_value_at_pos(oxy_report, pos)
        if common == 'tie' or common == '1':
            oxy_report = list(filter(lambda oxygen: oxygen[pos] == '1', oxy_report))
        elif common == '0':
            oxy_report = list(filter(lambda oxygen: oxygen[pos] == '0', oxy_report))

        if len(oxy_report) == 1:
            break
    return oxy_report[0]

def co2_generator(report):
    co2_report = report.copy()
    for pos in range(len(co2_report[0])):
        common = most_common_value_at_pos(co2_report, pos)
        if common == 'tie' or common == '1':
            co2_report = list(filter(lambda co2: co2[pos] == '0', co2_report))
        elif common == '0':
            co2_report = list(filter(lambda co2: co2[pos] == '1', co2_report))

        if len(co2_report) == 1:
            break
    return co2_report[0]

print(convert_binary_to_decimal(oxy_generator(report)) * convert_binary_to_decimal(co2_generator(report)))