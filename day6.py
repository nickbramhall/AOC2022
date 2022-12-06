day=6
input_type='test'

input_file = f'input/day{day}-{input_type}.txt'

# Read in all the data and strip out any whitespace at the end of lines
all_lines = [line.rstrip('\n') for line in open(input_file)]

print(all_lines)

buffer=''
c=0

for char in all_lines[1]:
    print(char)
    if len(buffer) < 4:
        buffer=buffer+char
    else:
        if char in buffer:
            buffer=buffer[:3]
            continue
        else:
            break
    print(buffer)
    c=c+1

print(c+1)