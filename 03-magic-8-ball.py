"""
Magic 8 Ball Project
REDDIT LINK: 
https://www.reddit.com/r/beginnerprojects/comments/29aqox/project_magic_8_ball/

GOAL
I'm sure you've used a magic 8 ball at some point in your life. You ask it a question, turn it right side up and it gives an answer by way of a floating die with responses written on it. You can create one in python. You must:
1. Allow the user to enter their question
2. Display an in progress message( i.e. "thinking")
3. Create 20 responses, and show a random response
4. Allow the user to ask another question or quit

BONUS: Using whatever module you like, add a gui. Your gui must have:
A box for users to enter the question
At least 4 buttons: Ask , clear(the text box), play again and quit(this must close the window)
"""
import random

def magic_8_ball(prompt):

  responses = [
    "It is certain.",
    "It is decidedly so.",
    "Without a doubt.",
    "Yes definitely.",
    "You may rely on it.",
    "As I see it, yes.",
    "Most likely.",
    "Outlook good.",
    "Yes.",
    "Signs point to yes.",
    "Reply hazy, try again.",
    "Ask again later.",
    "Better not tell you now.",
    "Cannot predict now.",
    "Concentrate and ask again.",
    "Don't count on it.",
    "My reply is no.",
    "My sources say no.",
    "Outlook not so good.",
    "Very doubtful.",
  ]

  question = input(prompt)

  if question != "quit":
    print("Hmm...")
    print(responses[random.randint(0, 20)])
    magic_8_ball("Would you like to ask another question or quit?\n")

magic_8_ball("What do you wish to know?\n")