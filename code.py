import random  # computer to pick a random choice
# List of possible choices
choices = ["rock", "paper", "scissors"]

# Computer randomly chooses
computer = random.choice(choices)

# Initialize player's choice
player = None

# Prevent choosing options other than rock, paper, or scissors
while player not in choices:
    player = input("rock, paper, or scissors?: ").lower()  # Convert input to lowercase

# Show what both the computer and player chose
    print("computer:", computer)
    print("player:", player)

# Determine the result of the game
    if player == computer:
        print("Tie!")
    elif player == 'rock':
        if computer == "paper":
            print("You lose! Paper covers Rock.")
        if computer == "scissors" :   #here in the place of this if we can keep else also
          # computer must be 'scissors'
            print("You win! Rock crushes Scissors.")
    elif player == 'scissors':
        if computer == "rock":
            print("You lose! Rock crushes Scissors.")
        if computer == "paper":  # computer must be 'paper'
            print("You win! Scissors cuts Paper.")
    elif player == 'paper':
        if computer == "scissors":
            print("You lose! Scissors cuts Paper.")
        if computer == "rock":  # computer must be 'rock'
            print("You win! Paper covers Rock.")

#here the print message is given to the player but not the computer

    play_again = input("Play again? (yes/no):").lower()
    if play_again == "yes" :
        print("All The Best!")
        break
    else:
        print("Bye!")
#this can also be written in as end of loop 
