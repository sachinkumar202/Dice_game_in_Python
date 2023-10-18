import random

# Set up the Ludo board
board = [
    [" ", " ", "G1", " ", " ", " ", "R1", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    ["G2", " ", " ", " ", " ", " ", " ", " ", " ", "R2"],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    ["R3", " ", " ", " ", " ", " ", " ", " ", " ", "G3"],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", "R4", " ", " ", " ", "G4", " ", " ", " "],
]

# Set up the players
players = ["Red", "Green"]
player_positions = [0, 0]  # Red starts at position 0, Green starts at position 0

# Set up the dice
dice = [1, 2, 3, 4, 5, 6]

# Game loop
while True:
    # Get the current player
    current_player = players[0]

    # Roll the dice
    input(f"{current_player}, press Enter to roll the dice...")
    dice_roll = random.choice(dice)

    # Update the player position
    player_positions[0] += dice_roll

    # Check if the player has won
    if player_positions[0] >= 40:
        print(f"{current_player} wins!")
        break

    # Update the board
    board[player_positions[0] // 10][player_positions[0] % 10] = "R1"

    # Print the board
    for row in board:
        print(row)

    # Swap players
    players[0], players[1] = players[1], players[0]
