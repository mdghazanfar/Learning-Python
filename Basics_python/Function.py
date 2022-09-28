# Def is short for define.
# Whenever you make a function, create a function, it's also called defining a function.

from __future__ import print_function
import re


def function():
  print("Hello Mrs! :)")

function()

#paramenter

def hello(name):
  print(f"hello {name}")

hello("MGA")

for x in range(5):
  hello("Shams")
  
def add_number(num1, num2):
  print(num1 + num2)

add_number(45,22)

def person_info(name, age):
  print(f"My name is {name} and i am {age} year old")

person_info("MGA", 22)

#return 

def double(number):
  return number*2

print(double(4))
new_variable = double(5)
print(new_variable)


def uppercase(text):
  return text.upper()

print(uppercase("ghazanfar"))

#Input 

user_name = input("enter you name:- ")

print(user_name)
print(user_name.upper())

user_num =input("what do you want to double? ")

print(user_num*2)
print(int(user_num)*2)
