# Python has a built-in module that you can use to make random numbers.
# The random module has a set of methods:

import random 
 
print(random.randint(1,10)), #intger number
print(random.random()), #float number


#print Yes, No or Maybe each time you ask it  randomly

answer = random.randint(1,3)

if answer == 1:
  print("yes")
if answer == 2:
  print("No")
if answer == 3:
  print("mayBe")




lucky_number = random.randint(1,100)
fortune_number = random.randint(1,3)
fortune_text = " "

if fortune_number == 1:
  fortune_text = "You'll have a great day!"
if fortune_number == 2:
  fortune_text = "today will be tough... but worth it!"
if fortune_number == 3:
  fortune_text = "You'll get merried this year!"

print(f"{fortune_text} Your lucky number is : {lucky_number}")
