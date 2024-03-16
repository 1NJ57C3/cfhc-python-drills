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

def generate_number():
  return random.randint(1, 100)

def gameloop(prompt, num, score=0):
  response = input(prompt + "\n> ").lower()

  def failure(direction):
    if score < 5:
      return flavor[random.randrange(3)] + direction
    elif score <= 10:
      return direction.capitalize()
    else:
      return flavor[random.randrange(3, len(flavor))] + direction.upper()

  try:
    int(response)
    if int(response) < num:
      gameloop(failure("higher"), num, score+1)
    elif int(response) > num:
      gameloop(failure("lower"), num, score+1)
    elif str(num) in response:
      print("Congratulations! You win and get... Nothing!")
      print("Guesses: " + str(score))
      response = input("Would you like to play again? (y/n)\n")
      if "y" in response.lower():
        gameloop("Here we go, again. 1 to 100. Hit me.", generate_number())
      else:
        print("Goodbye")
  except ValueError:
    if any(word in response for word in ["quit", "exit", "give up", "giving up"]) or response == "q":
      print(exit_messages[random.randrange(len(exit_messages))])
    else:
      gameloop(failed_validation[random.randrange(len(failed_validation))], num, score)

flavor = [
  "Aim ",
  "Try ",
  "Maybe ",
  "No. ",
  "Dude. ",
  "Bruh. ",
  "Come on! ",
]

failed_validation = [
  "Unless you're quitting, numbers only, please.",
  "You're supposed to give me a number.",
  "This is a NUMBER guessing game, idiot!",
]

exit_messages = [
  "Fine. I've got better things to do, anyway!",
  "Whatever.",
  "Okay, bye.",
  "Ugh.",
]

gameloop("I am thinking of a number between 1 and 100. Guess what it is. If you guess wrong, I'll give you a hint.", generate_number())
