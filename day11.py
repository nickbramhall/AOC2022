# Day 11: Monkey in the Middle

from copy import deepcopy

day=11
input_type='input'

input_file = f'input/day{day}-{input_type}.txt'

# Read in all the data and strip out any whitespace at the end of lines
all_lines = [line.rstrip('\n') for line in open(input_file)]

# Parse the input and build up a list of monkeys

monkeys=[]
counter=0
for line in all_lines:
    # print(line[:7])
    if line[:7] == 'Monkey ':
        monkeys.append({'inspections':0})
        continue
    elif line == '':
        counter=counter+1
        continue
    else:
        variable,data=line.split(': ')
        clean_variable=variable.strip()
        # print(f'Variable is "{variable}"')
        if clean_variable == "Starting items":
            # print(f'Adding items: {data}')
            list_of_items=data.split(', ')
            list_of_ints=[]
            for item in list_of_items:
                list_of_ints.append(int(item))
            monkeys[counter]['items']=list_of_ints
        if clean_variable == "Operation":
            new,equals,old,op,number=data.split(" ")
            monkeys[counter]['operation']=op
            if number == 'old':
                monkeys[counter]['operation_number']=number
            else:
                monkeys[counter]['operation_number']=int(number)
        if clean_variable == "Test":
            divisible,by,test_no=data.split(" ")
            monkeys[counter]['test']=int(test_no)
        if clean_variable == "If true":
            monkeys[counter]['true']=int(data[-1])
        if clean_variable == "If false":
            monkeys[counter]['false']=int(data[-1])

part1_monkeys=deepcopy(monkeys)
part2_monkeys=deepcopy(monkeys)

def MonkeyBusiness(monkeys,total_rounds):

    # Determine the appropriate common modulo operation number by multiplying all of the test values together 

    reducing_factor = 1

    for monkey in part2_monkeys:
        reducing_factor = reducing_factor * monkey['test']
    
    rounds=0
    while (rounds<total_rounds):
        for monkey in monkeys:
            items_counter=0
            if monkey['items']:
                for item in monkey['items']:
                    monkey['inspections']=monkey['inspections']+1
                    # Monkey inspects item
                    op_number = monkey['operation_number']
                    if op_number == 'old':
                        op_number = item
                    if monkey['operation'] == '*':
                        item=item * op_number
                    if monkey['operation'] == '+':
                        item=item + op_number
                    # Monkey gets bored
                    if total_rounds <= 20:
                        item = item // 3
                    else:
                        item = item % reducing_factor
                    # Throw test
                    throw_test = item % monkey['test']
                    if throw_test == 0:
                        monkeys[monkey['true']]['items'].append(item)
                    else:
                        monkeys[monkey['false']]['items'].append(item)
                    items_counter+=1
                for c in range (0,items_counter,1):
                    monkey['items'].pop(0)
        # Start of round
        
        rounds+=1

    return(monkeys)

def Result(list_of_monkeys):
    list_of_inspections=[]
    for monkey in list_of_monkeys:
        list_of_inspections.append(monkey['inspections'])
    list_of_inspections.sort(reverse=True)
    return list_of_inspections[0]*list_of_inspections[1]

# Part 1

part1_monkeys = MonkeyBusiness(part1_monkeys, 20)
part1 = Result(part1_monkeys)

print(f'Part 1: {part1}')

# Part 2

part2_monkeys = MonkeyBusiness(part2_monkeys, 10000)
part2 = Result(part2_monkeys)

print(f'Part 2: {part2}')