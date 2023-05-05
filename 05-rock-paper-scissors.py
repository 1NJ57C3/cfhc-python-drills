"""
Rock Paper Scissors
REDDIT LINK:
https://www.reddit.com/r/beginnerprojects/comments/2ah82f/rock_paper_scissors/

GOAL
You must make a rock paper scissors game
  1. Ask the player if they pick rock paper or scissors
  2. Have the computer chose its move
  3. Compare the choices and decide who wins
  4. Print the results

SUBGOALS
  - Let the player play again
  - Keep a record of the score e.g. (Player: 3 / Computer: 6)
"""
import random

score = {"player": 0, "computer": 0}

outcomes = {
  "rock": {
    "paper": "l",
    "scissors": "w"
  },
  "paper": {
    "rock": "w",
    "scissors": "l",
  },
  "scissors": {
    "rock": "l",
    "scissors": "w",
  }
}

def game():
  moves = ["rock", "paper", "scissors"]
  player_move = input(f'Choose: "{moves[0]}," "{moves[1]}," or "{moves[2]}?"\n> ').lower()
  system_move = moves[random.randrange(len(moves))]

  if player_move == system_move:
    print(f"You both played {player_move}. Tie game!")
  elif outcomes[player_move][system_move] == "w":
    print(f"Computer played {system_move}. You win!")
    score["player"] += 1
  elif outcomes[player_move][system_move] == "l":
    print(f"Computer played {system_move}. You lose!")
    score["computer"] += 1
  else:
    input("Invalid input")

  print(f"""
  Score:
  Player: {score["player"]}
  Computer: {score["computer"]}
  """)

  response = input("Play again? (y/n)\n> ")
  if response == "y":
    game()
  if response == "n":
    print("Goodbye")

game()