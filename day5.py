day=5
input_type='test'

input_file = f'input/day{day}-{input_type}.txt'

# Read in all the data and strip out any whitespace at the end of lines
all_lines = [line.rstrip('\n') for line in open(input_file)]

def clean_input(input_list):
    # Find where the commands start
    start_command=all_lines.index("")
    # Get list of commands
    commands_list=all_lines[start_command+1:]
    # Get contents of stacks
    stacks=all_lines[:start_command-1]
    # Turn the empty spots into single gaps
    clean_stacks=[]
    for row in stacks:
        split_row=row.split(" ")
        # print(split_row)
        i=0
        for entry in split_row:
            if entry == "":
                split_row.pop(i)
                split_row.pop(i)
                split_row.pop(i)
            i = i + 1
        # print(split_row)
        clean_stacks.append(split_row)
    #Transpose the cols and rows
    clean_stacks_t = [list(x) for x in zip(*clean_stacks)]
    # Reverse each row
    clean_stacks_r = []
    for i in range(len(clean_stacks_t)):
        clean_stacks_r.append(clean_stacks_t[i][::-1])
    # Now remove the extra "" on each line
    clean_stacks_final=[]
    for row in clean_stacks_r:
        try:
            end_of_goods=row.index("")
            clean_stacks_final.append(row[:end_of_goods])
        except:
            clean_stacks_final.append(row)
    
    return commands_list, clean_stacks_final

commands_list, stacks_part1 = clean_input(all_lines)

# Now go through commands

for command in commands_list:
    breakdown=command.split(" ")
    total_moves=int(breakdown[1])
    from_col=int(breakdown[3])-1
    to_col=int(breakdown[5])-1
    moves_made=0
    while(moves_made < total_moves):
        # print(f'move {moves_made} from {from_col} to {to_col}')
        # print(f'Before move: {stacks_part1}')
        try:
            result=stacks_part1[from_col].pop()
            stacks_part1[to_col].append(result)
        except:
            print('No valid move')
        # print(f'After move: {stacks_part1}')
        moves_made=moves_made+1

# print(stacks_part1)

message=''

for col in stacks_part1:
    try:
        message=message+col[-1]
    except:
        message=message+' '

message = message.replace("[", "")
message = message.replace("]", "") 

print(f'Part 1: "{message}"')

# Part 2 - starting with part2_clean_stacks

commands_list, stacks_part2 = clean_input(all_lines)

for command in commands_list:
    breakdown=command.split(" ")
    total_moves=int(breakdown[1])
    from_col=int(breakdown[3])-1
    to_col=int(breakdown[5])-1
    # Operation on origin stack
    # print(f'Before move: {stacks_part2}')
    # print(f'Move {total_moves} from {from_col} to {to_col}')
    moving_crates=stacks_part2[from_col][-total_moves:]
    # print(moving_crates)
    stacks_part2[from_col]=stacks_part2[from_col][:-total_moves]
    for item in moving_crates:
        # print(item)
        stacks_part2[to_col].append(item)
    # print(f'After move: {stacks_part2}')

message=''

for col in stacks_part2:
    try:
        message=message+col[-1]
    except:
        message=message+' '

message = message.replace("[", "")
message = message.replace("]", "") 

print(f'Part 2: "{message}"')

# Alt approach - https://github.com/PetchyAL/advent_of_code_2022/blob/main/solutions/day5/day5.py

# from string import ascii_uppercase
# import copy

# def prep_cargo(cargo):
#     prepped_cargo = [ [] for _ in range(3) ]
#     for row in cargo:
#         for c in range(len(row)):
#             #print(row[c])
#             if row[c] in ascii_uppercase:
#                 print(c//4)
#                 prepped_cargo[c//4].append(row[c])
#     return prepped_cargo

# with open("input/day5-test.txt") as text_file:
#     cargo, instructions = text_file.read().strip().split('\n\n')
# cargo = prep_cargo(cargo.split('\n'))

# print(cargo)