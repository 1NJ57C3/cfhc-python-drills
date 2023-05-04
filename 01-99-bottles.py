"""
99 Bottles of Beer On the Wall
REDDIT LINK
https://www.reddit.com/r/beginnerprojects/comments/19kxre/project_99_bottles_of_beer_on_the_wall_lyrics/

GOAL
Create a program that prints out every line to the song "99 bottles of beer on the wall." This should be a pretty simple program, so to make it a bit harder, here are some rules to follow.

RULES
- If you are going to use a list for all of the numbers, do not manually type them all in. Instead, use a built in function.
- Besides the phrase "take one down," you may not type in any numbers/names of numbers directly into your song lyrics.
- Remember, when you reach 1 bottle left, the word "bottles" becomes singular.
- Put a blank line between each verse of the song.
"""

def number_of_bottles(num):
  if num > 1:
    return str(num) + " bottles"
  if num == 1:
    return "Our very last bottle"
  elif num == 0:
    return "We drank all of the bottles"

def verse(x):
  return number_of_bottles(x) + " of beer on the wall\n" + number_of_bottles(x) + " of beer\nYou take one down, and pass it around\n" + number_of_bottles(x-1) + " of beer on the wall"

for x in range(99, 0, -1):
  if x > 1:
    print(verse(x) + "\n\n")
  else:
    print(verse(x))