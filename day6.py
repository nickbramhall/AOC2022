day=6
input_type='input'

input_file = f'input/day{day}-{input_type}.txt'

# Read in all the data and strip out any whitespace at the end of lines
all_lines = [line.rstrip('\n') for line in open(input_file)]

buffer=[]
c=0

# Function to determine whether the set of characters in the buffer is unique

def unique(input_buffer,length_of_message):
    # insert the list to the set
    list_set = set(input_buffer)
    # convert the set to the list
    unique_list = (list(list_set))
    if len(unique_list) == length_of_message:
        print(f'{unique_list} has {length_of_message} unique entries')
        return True
    else:
        return False

# Part 1

for char in all_lines[0]:
    # Build up the buffer to 4 characters total
    if len(buffer) < 4:
        buffer.append(char)
    # Once the buffer is full check for uniqueness
    else:
        unique_check = unique(buffer,4)
        if unique_check is True:
            # If all characters are unique, stop and get the current count value
            break
        else:
            # If not unique then we need to move the buffer one along, drop the first entry, add the current char
            buffer=buffer[1:]
            buffer.append(char)
    c=c+1

print(f'Part 1: {c}')

# Part 2 - repeats the above but with a buffer of 14 rather than 4

buffer=[]
c=0

for char in all_lines[0]:
    if len(buffer) < 14:
        buffer.append(char)
    else:
        unique_check = unique(buffer,14)
        if unique_check is True:
            break
        else:
            buffer=buffer[1:]
            buffer.append(char)
    c=c+1

print(f'Part 2: {c}')