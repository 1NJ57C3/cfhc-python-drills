"""
Higher/Lower Guessing Game
REDDIT LINK:
https://www.reddit.com/r/beginnerprojects/comments/19jj9a/project_higherlower_guessing_game/

GOAL 
  Create a simple game where the computer randomly selects a number between 1 and 100 and the user has to guess what the number is. After every guess, the computer should tell the user if the guess is higher or lower than the answer. When the user guesses the correct number, print out a congratulatory message.

SUBGOALS
1. Add an introduction message that explains to the user how to play your game.
2. In addition to the congratulatory message at the end of the game, also print out how many guesses were taken before the user arrived at the correct answer.
3. At the end of the game, allow the user to decide if they want to play again (without having to restart the program).
"""
import random

HINT_FLAVOR = [
  "Aim ",
  "Try ",
  "Maybe ",
  "No. ",
  "Dude. ",
  "Bruh. ",
  "Come on! ",
  "Seriously?! ",
  "How are we still doing this?! ",
]

VALIDATION_ERRORS = [
  "Unless you're quitting, numbers only, please.",
  "You're supposed to give me a number.",
  "This is a NUMBER guessing game, idiot!",
]

EXIT_PHRASES = ["quit", "exit", "give up", "giving up"]

EXIT_RESPONSES = [
  "Fine. I've got better things to do, anyway!",
  "Whatever.",
  "Okay, bye.",
  "Ugh.",
]

def generate_number():
  return random.randint(1, 100)

def game_loop(prompt, num, score=0):
  response = input(prompt + "\n> ").lower()

  def retry_prompt(direction):
    if score < 5:
      return HINT_FLAVOR[random.randrange(3)] + direction
    elif score <= 10:
      return direction.capitalize()
    else:
      return HINT_FLAVOR[random.randrange(3, len(HINT_FLAVOR))] + direction.upper()

  def victory_prompt():
    print("Congratulations! You win and get... Nothing!")
    print("Guesses: " + str(score))
    response = input("Would you like to play again? (y/n)\n")
    if "y" in response:
      game_loop("Here we go, again. 1 to 100. Hit me.", generate_number())
    else:
      print("Goodbye")

  if any(exit_phrase in response for exit_phrase in EXIT_PHRASES) or response == "q":
    print(EXIT_RESPONSES[random.randrange(len(EXIT_RESPONSES))])
  else:
    try:
      int(response)
    except ValueError:
      game_loop(VALIDATION_ERRORS[random.randrange(len(VALIDATION_ERRORS))], num, score)
    else:
      if int(response) < num:
        game_loop(retry_prompt("higher"), num, score + 1)
      elif int(response) > num:
        game_loop(retry_prompt("lower"), num, score + 1)
      elif str(num) in response:
        victory_prompt()

game_loop("I am thinking of a number between 1 and 100. Guess what it is. If you guess wrong, I'll give you a hint.", generate_number())
