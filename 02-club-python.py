"""
Club Python
GOAL
You run a club, and would like to save money on hiring human staff,
so you write a virtual “bouncer” program. This bouncer asks the user's
age, and if they are under the age of 18, they are not allowed access.

RULES
1. Have the bouncer ask the user's age.
2. If their age is above 18, have the bouncer allow them in.
3. If their age is below 18, have the bouncer reject them entry.
"""

def bouncer (age = int(input('Enter age:'))):
  if age < 18:
    print("YOU SHALL NOT PASS!")
  else:
    print("Go ahead")

bouncer()