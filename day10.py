# Day 10: Cathode-Ray Tube

day=10
input_type='input'

input_file = f'input/day{day}-{input_type}.txt'

# Read in all the data and strip out any whitespace at the end of lines
all_lines = [line.rstrip('\n') for line in open(input_file)]

# Cycle   1 -> ######################################## <- Cycle  40
# Cycle  41 -> ######################################## <- Cycle  80
# Cycle  81 -> ######################################## <- Cycle 120
# Cycle 121 -> ######################################## <- Cycle 160
# Cycle 161 -> ######################################## <- Cycle 200
# Cycle 201 -> ######################################## <- Cycle 240

crt = [['░']*40 for i in range(6)]

def pixel(cycle,register):
    col = (cycle % 40)-1
    row = cycle // 40
    sprite_pixels = (register-1,register,register+1)
    if col in sprite_pixels:
        crt[row][col] = '█'

register=1
signal_strength=0
cycle=1

target_cycles=(20,60,100,140,180,220)
screen_string=''

end_of_file = False

while end_of_file is False:

    # Check for signal strength
    if cycle in target_cycles:
        print(f'Cycle: {cycle} -- Register: {register}')
        signal_strength=signal_strength+(cycle*register)
    
    # Get the current pixel value and add to the screen string for later use
    screen_string=pixel(cycle,register)

    # Now get the next command and process it
    if all_lines[0] == "noop":
        all_lines.pop(0)
    else:
        command,value=all_lines[0].split(" ")
        if command == "addx":
            all_lines.pop(0)
            all_lines.insert(0, f'addy {value}')
        else:
            register=register+int(value)
            all_lines.pop(0)
    
    # Increase the cycle count
    cycle+=1
    
    # If we have reached the end of the code then set End of File to True to exit the while loop
    if not all_lines:
        print('End of file')
        end_of_file = True

print(f'Part 1: {signal_strength}')
# Find the signal strength during the 20th, 60th, 100th, 140th, 180th, and 220th cycles.

# Part 2

for row in crt: #Part 2 result
  print(''.join(row))