day=4
input_type='input'

input_file = f'input/day{day}-{input_type}.txt'

# Read in all the data and strip out any whitespace at the end of lines
all_lines = [line.rstrip('\n') for line in open(input_file)]

# print(all_lines)

count=0

for line in all_lines:
    elf1,elf2=line.split(',')
    elf1_start,elf1_stop=elf1.split('-')
    elf2_start,elf2_stop=elf2.split('-')
    elf1_start=int(elf1_start)
    elf1_stop=int(elf1_stop)
    elf2_start=int(elf2_start)
    elf2_stop=int(elf2_stop)
    if elf1_start == elf1_stop:
        if elf1_start == elf2_start or elf1_start == elf2_stop:
            # print(f'Match found for {elf1},{elf2}')
            count = count + 1
            continue
    if elf2_start == elf2_stop:
        if elf2_start == elf1_start or elf2_start == elf1_stop:
            # print(f'Match found for {elf1},{elf2}')
            count = count + 1
            continue
    if elf1_start <= elf2_start:
        if elf1_stop >= elf2_stop:
            # print(f'Match found for {elf1},{elf2}')
            count = count + 1
            continue
    if elf1_start >= elf2_start:
        if elf1_stop <= elf2_stop:
            # print(f'Match found for {elf1},{elf2}')
            count = count + 1
            continue
    # print('\n')
    # print('.'*(elf1_start-1)+'X'*(elf1_stop-elf1_start+1)+'.'*(100-elf1_stop))
    # print('.'*(elf2_start-1)+'X'*(elf2_stop-elf2_start+1)+'.'*(100-elf2_stop))
    # print(f'No match found for {elf1},{elf2}')

print(f'Part 1: {count}')

# Part 2

count=0

for line in all_lines:
    elf1,elf2=line.split(',')
    elf1_start,elf1_stop=elf1.split('-')
    elf2_start,elf2_stop=elf2.split('-')
    elf1_start=int(elf1_start)
    elf1_stop=int(elf1_stop)
    elf2_start=int(elf2_start)
    elf2_stop=int(elf2_stop)
    if elf2_start <= elf1_start <= elf2_stop:
        count = count + 1
        continue
    if elf1_start <= elf2_start <= elf1_stop:
        count = count + 1
        continue

print(f'Part 2: {count}')