day=8
input_type='input'

input_file = f'input/day{day}-{input_type}.txt'

# Read in all the data and strip out any whitespace at the end of lines
newLineList = [line.rstrip('\n') for line in open(input_file)]

# print(all_lines)

total_cols = len(newLineList[0])
total_rows = len(newLineList)

visible_counter = total_cols*2 + total_rows*2 - 4

search_results={}
scenic_score_result=0

for start_row in range(1,total_rows-1,1):

    for start_col in range(1,total_cols-1,1):

        tree_value=(newLineList[start_row][start_col])

        # print(f'Check tree at {start_row},{start_col} : {tree_value}')

        # walk up
        row=start_row-1
        col=start_col

        up_visible=True
        up_counter=0

        while row > -1:
            search_tree = newLineList[row][col]
            # print(search_tree)
            if up_visible is True:
                up_counter = up_counter + 1
            if search_tree >= tree_value:
                up_visible = False
            row=row-1

        # walk down
        row=start_row+1
        col=start_col

        down_visible=True
        down_counter=0

        while row < total_rows:
            search_tree = newLineList[row][col]
            # print(search_tree)
            if down_visible is True:
                down_counter = down_counter + 1
            if search_tree >= tree_value:
                down_visible = False
            row=row+1

        # walk left
        row=start_row
        col=start_col-1

        left_visible=True
        left_counter=0

        while col > -1:
            search_tree = newLineList[row][col]
            if left_visible is True:
                left_counter = left_counter + 1
            if search_tree >= tree_value:
                left_visible = False
            col=col-1

        # walk right
        row=start_row
        col=start_col+1

        right_visible=True
        right_counter=0

        while col < total_cols:
            search_tree = newLineList[row][col]
            if right_visible is True:
                right_counter = right_counter + 1
            if search_tree >= tree_value:
                right_visible = False
            col=col+1

        # Part 1 - updating visible counter if visibility is ok in at least one direction
        if up_visible is True or down_visible is True or left_visible is True or right_visible is True:
            search_results[(start_row,start_col)]=True
            visible_counter=visible_counter+1
        else:
            search_results[(start_row,start_col)]=False
        
        # Part 2 - updating scenic score if it beats the current highest score
        scenic_score= up_counter * down_counter * left_counter * right_counter
        if scenic_score > scenic_score_result:
            scenic_score_result = scenic_score

print(f'Part 1: {visible_counter}')
print(f'Part 2: {scenic_score_result}')