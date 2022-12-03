input_file = 'input/day3-input.txt'

# Read in all the data and strip out any whitespace at the end of lines
all_lines = [line.rstrip('\n') for line in open(input_file)]

print(all_lines)

priority_lookup={'a':1, 'b':2,'c':3,'d':4,'e':5,'f':6,
                'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,
                'm':13,'n':14,'o':15,'p':16,'q':17,'r':18,
                's':19,'t':20,'u':21,'v':22,'w':23,'x':24,
                'y':25,'z':26,
                'A':27, 'B':28,'C':29,'D':30,'E':31,'F':32,
                'G':33,'H':34,'I':35,'J':36,'K':37,'L':38,
                'M':39,'N':40,'O':41,'P':42,'Q':43,'R':44,
                'S':45,'T':46,'U':47,'V':48,'W':49,'X':50,
                'Y':51,'Z':52}

total_score = 0

for line in all_lines:
    length_of_line = len(line)
    # print(length_of_line)
    items_in_compartment_A = line[0:length_of_line/2]
    items_in_compartment_B = line[length_of_line/2:]
    # print(items_in_compartment_B)
    item_found = False
    for item in items_in_compartment_A:
        if item_found is False:
            # print(item)
            result = items_in_compartment_B.find(item)
            if result != -1:
                # print(item)
                score = priority_lookup[item]
                # print(score)
                total_score = total_score + score
                item_found = True

print(total_score)

## Part 2

chunked_list = list()
chunk_size = 3

for i in range(0, len(all_lines), chunk_size):
    chunked_list.append(all_lines[i:i+chunk_size])

print(chunked_list)

total_score = 0

for group_of_eleves in chunked_list:
    rucksack_A = group_of_eleves[0]
    rucksack_B = group_of_eleves[1]
    rucksack_C = group_of_eleves[2]
    # print(rucksack_A)
    item_found = False
    for item in rucksack_A:
        # print(item)
        if item_found is False:
            result_B = rucksack_B.find(item)
            result_C = rucksack_C.find(item)
            if result_B != -1 and result_C != -1:
                # Item found
                # print(item)
                score = priority_lookup[item]
                total_score = total_score + score
                item_found = True

print(total_score)
