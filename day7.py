day=7
input_type='input'

input_file = f'input/day{day}-{input_type}.txt'

# Read in all the data and strip out any whitespace at the end of lines
all_lines = [line.rstrip('\n') for line in open(input_file)]

# print(all_lines)

# Part 1 - determine the total size of each directory

breadcrumbs=[] # Use this to make unique directory names
directories={} # Store dict of every directory
size={} # Store file and directory contents info

for input in all_lines:
    input_split = input.split(" ")
    if input_split[0] == "$":
        # It is a command
        if input_split[1] == 'cd':
            if input_split[2] == '..':
                # Go up
                breadcrumbs.pop()
                # print(breadcrumbs)
            else:
                # Go down to next directory
                breadcrumbs.append(input_split[2])
                # print(breadcrumbs)
                dir_name=''
                for entry in breadcrumbs:
                    dir_name=dir_name+entry
                directories[dir_name]=[]
                size[dir_name]=0
    else:
        if input_split[0] == "dir":
            directory_name=input_split[1]
            # print(f'Directory: {directory_name}')
            dir_name=''
            for entry in breadcrumbs:
                dir_name=dir_name+entry
            directories[dir_name].append('dir '+dir_name+directory_name)
        else:
            #It is a file
            file_size=int(input_split[0])
            file_name=input_split[1]
            dir_name=''
            for entry in breadcrumbs:
                dir_name=dir_name+entry
            directories[dir_name].append(input)
            size[dir_name] = size[dir_name] + int(file_size)

# Now run through the dictionary in reverse to get all the sizes

for k,v in reversed(list(directories.items())):
    # print(f'Directory: {k}')
    current_directory=k
    size[current_directory]=0
    for entry in v:
        # print(f'Current file: "{entry[:3]}" -> "{entry[4:]}"')
        if entry[:3] == 'dir':
            # print('Found directory')
            size[current_directory] = size[current_directory] + size[entry[4:]]
        else:
            file_size, file_name=entry.split(" ")
            size[current_directory] = size[current_directory] + int(file_size)
    # print(sizing)

# print(size)

total_size=0

for k,v in size.items():
    if v <= 100000:
        total_size = total_size + v

print(f'Part 1: {total_size}')

# Part 2

total_space = 70000000
update_required = 30000000

total_installed = size['/']
free_space = total_space - total_installed
space_required = update_required - free_space

# Use the size dictionary to find smallest directory to be deleted

# Order the dictionary by size from smallest to largest

sorted_size = {k: v for k, v in sorted(size.items(), key=lambda item: item[1])}

# Now iterate through and test against space_required

for k,v in sorted_size.items():
    if v > space_required:
        print(f'Part 2: {v}')
        break