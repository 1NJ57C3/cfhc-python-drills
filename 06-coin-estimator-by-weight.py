"""
Coin Estimator By Weight
REDDIT LINK
https://www.reddit.com/r/beginnerprojects/comments/1idqw1/project_coin_estimator_by_weight/

BACKGROUND
When some people receive change after shopping, they put it into a container and let it add up over time. Once they fill up the container, they'll roll them up in coin wrappers which can then be traded in at a bank for what they are worth. While most banks will give away coin wrappers for free, it's convenient to have an idea of how many you will need. Instead of counting how many coins you have, it's easier to separate all of your coins, weigh them, and then estimate how many of each type you have and then how many wrappers you'll need.
For example, if you weigh all of your dimes and see that you have 1276.9g of them, you can estimate that you have about 563 dimes (since each one is 2.268g) and you would be able to fill 11 dime wrappers.

GOAL
  1. Create a program that allows the user to input the total weight of each type of coin they have (pennies, nickels, dimes, and quarters)
  2. Print out how many of each type of wrapper they would need, how many coins they have, and the estimated total value of all of their money.
  3. Give the weight of each coin and how many fit inside each type of wrapper.

SUBGOALS
  - Round all numbers printed out to the nearest whole number.
  - Allow the user to select whether they want to submit the weight in either grams or pounds.
"""
import re
import functools

class Coin:
  def __init__(self, name, name_plural, weight, value, units_per_wrapper, total_weight=0, quantity=0):
    self.name = name
    self.name_plural = name_plural
    self.weight = weight
    self.value = value
    self.units_per_wrapper = units_per_wrapper
    self.total_weight = total_weight

  def update_total_weight(self, value):
    self.total_weight = value

  @property
  def quantity(self):
    return round(self.total_weight / self.weight)
  
  @property
  def wrappers_needed(self):
    return self.quantity / self.units_per_wrapper
  
  @property
  def total_value(self):
    return self.quantity * self.value
  
  @property
  def attributes(self):
    return {
      "name": self.name,
      "name_plural": self.name_plural,
      "weight": self.weight,
      "value": self.value,
      "units_per_wrapper": self.units_per_wrapper,
      "total_weight": self.total_weight,
      "wrappers_needed": self.wrappers_needed,
      "quantity": self.quantity,
      "total_value": self.total_value
    }

pennies = Coin(name="penny", name_plural="pennies", weight=2.5, units_per_wrapper=50, value=0.01)
nickels = Coin(name="nickel", name_plural="nickels", weight=5.0, units_per_wrapper=40, value=0.05)
dimes = Coin(name="dime", name_plural="dimes", weight=2.268, units_per_wrapper=50, value=0.10)
quarters = Coin(name="quarter", name_plural="quarters", weight=5.67, units_per_wrapper=40, value=0.25)
half_dollars = Coin(name="half dollar", name_plural="half dollars", weight=11.34, units_per_wrapper=20, value=0.50)
dollars = Coin(name="small dollar", name_plural="small dollars", weight=8.1, units_per_wrapper=25, value=1.00)

coins = {
  "pennies": pennies,
  "nickles": nickels,
  "dimes": dimes,
  "quarters": quarters,
  "half dollars": half_dollars,
  "small dollars": dollars,
}

grams_per_pound = 453.592
pounds_per_gram = 1 / grams_per_pound

def to_lbs(grams):
  return grams * pounds_per_gram

def to_g(pounds):
  return pounds * grams_per_pound


def set_measurement():
  user_input = input("\nPlease select unit of measurement: \n grams (g)\n pounds (lbs)?\n> ")
  if re.search("^g", user_input):
    return "g"
  elif re.search("pound|lb", user_input):
    return "lbs"
  else: 
    print("\nError: Input not recognized.")
    return set_measurement()

def get_total_weight(coin):
  user_input = input(f"\nPlease enter total numerical weight of {coin}.\n> ")

  if re.search("^[0-9]*\.?[0-9]+$", user_input):
    return float(user_input)
  else:
    print("\nError: Input must be a number.")
    return get_total_weight(coin)

def generate_output(name, name_plural, weight, value, units_per_wrapper, total_weight, wrappers_needed, quantity, total_value, unit_of_measurement):
  weight_spacer = ""

  if unit_of_measurement == "lbs":
    total_weight = to_lbs(total_weight)
    weight = to_lbs(weight)
    weight_spacer = " "

  return (
    "\n" +
    f"{name_plural.title()}\n" + 
    f"  Weight entered: {total_weight}{weight_spacer}{unit_of_measurement}\n" + 
    f"  Unit weight: {weight}{weight_spacer}{unit_of_measurement}\n" + 
    f"  Estimated quantity: {quantity}\n" +
    f"  {units_per_wrapper} {name_plural} fit into a standard {name} wrapper.\n" + 
    f"  Wrappers needed: {wrappers_needed}\n" +
    f"  Estimated cash value: {total_value:.2f}\n" +
    "\n"
  )

"""
Actual output code starts here
"""
unit_of_measurement = set_measurement()

for coin in coins:
  coin_obj = coins[coin]
  weight_input = get_total_weight(coin)

  if unit_of_measurement == "lbs":
    weight_input = to_g(weight_input)

  coin_obj.update_total_weight(weight_input)
  print(generate_output(**coin_obj.attributes, unit_of_measurement=unit_of_measurement))

print("Total")
print("  Coins: " + str(functools.reduce(lambda accumulator, coin: accumulator + coins[coin].quantity, coins, 0)))
print("  Cash Value: " + str(functools.reduce(lambda accumulator, coin: accumulator + coins[coin].total_value, coins, 0)) + "\n")