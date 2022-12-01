input_file = 'day1-input.txt'

# Read in all the data and strip out any whitespace at the end of lines
all_lines = [line.rstrip('\n') for line in open(input_file)]

# Create an empty list to hold all of the calorie values for each elf
all_elfs_calorie_totals = []
# Set a counter for the elf's calories
elf_calorie_count=0

# Read through each line to determine whether it is added to the current total or if it is a new elf
for line in all_lines:
    if line != "":
        elf_calorie_count = elf_calorie_count + int(line)
    else:
        all_elfs_calorie_totals.append(elf_calorie_count)
        # Reset the calories counter
        elf_calorie_count=0

# Append the final elf's calories to the list
all_elfs_calorie_totals.append(elf_calorie_count)

# Now get the highest calories value in the list using max()
print(f'The answer to Part 1 is: {max(all_elfs_calorie_totals)} calories')

## Part 2

# Sort the list of calories values so that the highest are at the beginning
all_elfs_calorie_totals.sort(reverse=True)

# Now splice off the first three entries - these are the highest three
top_three_elves = all_elfs_calorie_totals[0:3]

# Now sum up the list of the three highest values to get the answer for Part 2
top_three_calories = sum(top_three_elves)

print(f'The answer to Part 2 is: {top_three_calories} calories')