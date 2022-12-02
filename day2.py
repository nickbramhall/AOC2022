input_file = 'input/day2-input.txt'

# Read in all the data and strip out any whitespace at the end of lines
all_lines = [line.rstrip('\n') for line in open(input_file)]

## Part 1 ##

# A: Rock, B: Paper, C: Scissors
# X: Rock, Y: Paper, Z: Scissors

enemy_shape_score = {'A':1,'B':2,'C':3}
player_shape_score = {'X':1,'Y':2,'Z':3}

def game_outcome(enemy, player):
    enemy_score = enemy_shape_score[enemy]
    player_score = player_shape_score[player]
    if enemy_score == 1 and player_score == 3:
        score = 0
    elif enemy_score == 3 and player_score == 2:
        score = 0
    elif enemy_score == 2 and player_score == 1:
        score = 0
    elif enemy_score == 3 and player_score == 1:
        score = 6
    elif enemy_score == 2 and player_score == 3:
        score = 6
    elif enemy_score == 1 and player_score == 2:
        score = 6
    else:
        score = 3
    return score

total_score = 0

for line in all_lines:
    enemy, player = line.split(" ")
    # Get player score
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

# Reset the total_score for Part 2
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
    # Get the game score based on the outcome
    game_score = outcome_score[outcome]
    # Get the player score based on the enemy play and the desired outcome
    player_score = correct_play(enemy, outcome)
    # Combine the player score and game score to get the round score
    round_score = player_score + game_score
    # Add the round score to the total score for all of the rounds
    total_score = total_score + round_score
    
print(f'Part 2: {total_score}')