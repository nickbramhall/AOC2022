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

def pixel(cycle,register):
    sprite_pixels=(register-1,register,register+1)
    lit=False
    if cycle < 41:
        if cycle in sprite_pixels:
            lit = True
    elif cycle < 81:
        if cycle-40 in sprite_pixels:
            lit = True
    elif cycle < 121:
        if cycle-80 in sprite_pixels:
            lit = True
    elif cycle < 161:
        if cycle-120 in sprite_pixels:
            lit = True
    elif cycle < 201:
        if cycle-160 in sprite_pixels:
            lit = True
    else:
        if cycle-200 in sprite_pixels:
            lit = True
    if lit is True:
        return '█'
    else:
        return '░'

register=1
signal_strength=0
cycle=1

target_cycles=(20,60,100,140,180,220)
screen_string=''

end_of_file = False

while end_of_file is False:
    # print(f'Cycle: {cycle} Command: {all_lines[0]}')
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
    
    # Get the current pixel value and add to the screen string for later use
    screen_string=screen_string+pixel(cycle,register)

    # Increase the cycle count
    cycle+=1
    
    if cycle in target_cycles:
        print(f'Cycle: {cycle} -- Register: {register}')
        signal_strength=signal_strength+(cycle*register)
    
    # If we have reached the end of the code then set End of File to True to exit the while loop
    if not all_lines:
        print('End of file')
        end_of_file = True

print(f'Part 1: {signal_strength}')
# Find the signal strength during the 20th, 60th, 100th, 140th, 180th, and 220th cycles.

# Part 2

c=0
for pixel in screen_string:
    if c in (39,79,119,159,199,239):
        print(pixel)
    else:
        print(pixel, end="")
    c=c+1