input_file = 'input/day2-input.txt'

# Read in all the data and strip out any whitespace at the end of lines
all_lines = [line.rstrip('\n') for line in open(input_file)]

## Part 1 ##

# A: Rock, B: Paper, C: Scissors
# X: Rock, Y: Paper, Z: Scissors

enemy_shape_score = {'A':1,'B':2,'C':3}
player_shape_score = {'X':1,'Y':2,'Z':3}

def game_outcome(enemy, player):
    enemy_win = False
    player_win = False
    draw = False
    enemy_score = enemy_shape_score[enemy]
    player_score = player_shape_score[player]
    if enemy_score == 1 and player_score == 3:
        enemy_win = True
    elif enemy_score == 3 and player_score == 2:
        enemy_win = True
    elif enemy_score == 2 and player_score == 1:
        enemy_win = True
    elif enemy_score == 3 and player_score == 1:
        player_win = True
    elif enemy_score == 2 and player_score == 3:
        player_win = True
    elif enemy_score == 1 and player_score == 2:
        player_win = True
    else:
        draw = True
    if enemy_win:
        score = 0
    if player_win:
        score = 6
    if draw:
        score = 3
    return score

total_score = 0

for line in all_lines:
    enemy, player = line.split(" ")
    # Get your score
    player_score = player_shape_score[player]
    # Get the score for the outcome
    game_score = game_outcome(enemy, player)
    # Combine the player score and game score to get the round score
    round_score = player_score + game_score
    # Add the round score to the total score for all of the rounds
    total_score = total_score + round_score
    
print(f'Part 1: {total_score}')

## Part 2 ##

# A: Rock, B: Paper, C: Scissors
# X: Lose, Y: Draw, Z: Win

outcome_score = {'X':0,'Y':3,'Z':6}

total_score = 0

def correct_play(enemy, outcome):
    enemy_score = enemy_shape_score[enemy]
    desired_outcome = player_shape_score[outcome]
    if enemy_score == 1:
        if desired_outcome == 1:
            player_shape = 3
        if desired_outcome == 2:
            player_shape = 1
        if desired_outcome == 3:
            player_shape = 2
    if enemy_score == 2:
        if desired_outcome == 1:
            player_shape = 1
        if desired_outcome == 2:
            player_shape = 2
        if desired_outcome == 3:
            player_shape = 3
    if enemy_score == 3:
        if desired_outcome == 1:
            player_shape = 2
        if desired_outcome == 2:
            player_shape = 3
        if desired_outcome == 3:
            player_shape = 1
    return player_shape

for line in all_lines:
    enemy, outcome = line.split(" ")
    # Get the game score
    game_score = outcome_score[outcome]
    player_score = correct_play(enemy, outcome)
    round_score = player_score + game_score
    total_score = total_score + round_score
    
print(f'Part 2: {total_score}')