day=9
input_type='input'

input_file = f'input/day{day}-{input_type}.txt'

# Read in all the data and strip out any whitespace at the end of lines
all_lines = [line.rstrip('\n') for line in open(input_file)]

# print(all_lines)

def tail_movement(head_position,tail_position):
    x_axis_diff=head_position[0]-tail_position[0]
    y_axis_diff=head_position[1]-tail_position[1]
    # print(f'xdiff: {x_axis_diff}')
    # print(f'ydiff: {y_axis_diff}')
    # print(f'Head position: {head_position} -- Start tail position: {tail_position} -- Xdiff: {x_axis_diff} -- Ydiff: {y_axis_diff}')
    if x_axis_diff > 1 and y_axis_diff > 1:
        #print('Big jump!')
        tail_position[0]=head_position[0]-1
        tail_position[1]=head_position[1]-1
    elif x_axis_diff < -1 and y_axis_diff > 1:
        #print('Big jump!')
        tail_position[0]=head_position[0]+1
        tail_position[1]=head_position[1]-1
    elif x_axis_diff < -1 and y_axis_diff < -1:
        #print('Big jump!')
        tail_position[0]=head_position[0]+1
        tail_position[1]=head_position[1]+1
    elif x_axis_diff > 1 and y_axis_diff < -1:
        #print('Big jump!')
        tail_position[0]=head_position[0]-1
        tail_position[1]=head_position[1]+1
    else:
        if x_axis_diff > 1:
            tail_position[0]=head_position[0]-1
            tail_position[1]=head_position[1]
        if x_axis_diff < -1:
            tail_position[0]=head_position[0]+1
            tail_position[1]=head_position[1]
        if y_axis_diff > 1:
            tail_position[0]=head_position[0]
            tail_position[1]=head_position[1]-1
        if y_axis_diff < -1:
            tail_position[0]=head_position[0]
            tail_position[1]=head_position[1]+1
    return tail_position

def update_tail_visited(tail_position):
    tail_visited.add((tail_position[0],tail_position[1]))
    return True

# Part 1

head_position=[0,0]
tail_position=[0,0]

tail_visited = set()

for move in all_lines:
    direction,distance=move.split(" ")
    distance=int(distance)
    if direction == "R":
        for _ in range(head_position[0],head_position[0]+distance,1):
            head_position[0]=head_position[0]+1
            tail_position=tail_movement(head_position,tail_position)
            update_tail_visited(tail_position)
    if direction == "L":
        for _ in range(head_position[0],head_position[0]-distance,-1):
            head_position[0]=head_position[0]-1
            tail_position=tail_movement(head_position,tail_position)
            update_tail_visited(tail_position)
    if direction == "U":
        for _ in range(head_position[1],head_position[1]+distance,1):
            head_position[1]=head_position[1]+1
            tail_position=tail_movement(head_position,tail_position)
            update_tail_visited(tail_position)
    if direction == "D":
        for _ in range(head_position[1],head_position[1]-distance,-1):
            head_position[1]=head_position[1]-1
            tail_position=tail_movement(head_position,tail_position)
            update_tail_visited(tail_position)

print(f'Part 1: {len(tail_visited)}')

## Part 2

head_position=[0,0]
knot_positions=[[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]

knots=[0,1,2,3,4,5,6,7,8]

tail_visited=set()

for move in all_lines:
    direction,distance=move.split(" ")
    distance=int(distance)
    if direction == "R":
        for _ in range(head_position[0],head_position[0]+distance,1):
            head_position[0]=head_position[0]+1
            for k in knots:
                if k-1 < 0:
                    knot_positions[k]=tail_movement(head_position,knot_positions[k])
                else:
                    knot_positions[k]=tail_movement(knot_positions[k-1],knot_positions[k])
            update_tail_visited(knot_positions[8])
    if direction == "L":
        for _ in range(head_position[0],head_position[0]-distance,-1):
            head_position[0]=head_position[0]-1
            for k in knots:
                if k-1 < 0:
                    knot_positions[k]=tail_movement(head_position,knot_positions[k])
                else:
                    knot_positions[k]=tail_movement(knot_positions[k-1],knot_positions[k])
            update_tail_visited(knot_positions[8])
    if direction == "U":
        for _ in range(head_position[1],head_position[1]+distance,1):
            head_position[1]=head_position[1]+1
            for k in knots:
                if k-1 < 0:
                    knot_positions[k]=tail_movement(head_position,knot_positions[k])
                else:
                    knot_positions[k]=tail_movement(knot_positions[k-1],knot_positions[k])
            update_tail_visited(knot_positions[8])
    if direction == "D":
        for _ in range(head_position[1],head_position[1]-distance,-1):
            head_position[1]=head_position[1]-1
            for k in knots:
                if k-1 < 0:
                    knot_positions[k]=tail_movement(head_position,knot_positions[k])
                else:
                    knot_positions[k]=tail_movement(knot_positions[k-1],knot_positions[k])
            update_tail_visited(knot_positions[8])

print(f'Part 2: {len(tail_visited)}')