#string 

from re import L
from traceback import print_tb

#What letter do we put in front of a String if we want to put variables in it?
#Answer = f;

store = 'Nick\'s Pizza shop, the "best" there is'
print(store)




#Boolean and if statements

day = 19 #Number
weight = 152.12 #float
month ='September' #string

light_is_on = False #Booleans can only be True or False. They are binary. Yes or no. 1 or 0.

if light_is_on:
    print("light is on! ")
else:
    print("We're in the dark!")

weight = 190.2

if weight < 195:          # using more conditation like <,>,>=,==,etc...
  print("You're in under weight :)") 

  
  age = 32 
  if age >= 18:
    print("Adult")
  else:
    print("You're  child")