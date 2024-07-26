# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

def player(prev_play, opponent_history=[]):
    if prev_play != "":
        opponent_history.append(prev_play)
    
    n = 3  # Size of the sequence to track
    guess = "R"
    
    if len(opponent_history) >= n:
        seq = "".join(opponent_history[-n:])
        next_move_freq = {
            "R": 0,
            "P": 0,
            "S": 0,
        }
        
        # Track the frequency of moves after the sequence
        for i in range(len(opponent_history) - n):
            if "".join(opponent_history[i:i + n]) == seq:
                next_move_freq[opponent_history[i + n]] += 1
        
        # Predict the next move based on frequency
        if sum(next_move_freq.values()) > 0:
            guess = max(next_move_freq, key=next_move_freq.get)
    
    # Counter the predicted move
    counter = {"R": "P", "P": "S", "S": "R"}
    return counter[guess]
