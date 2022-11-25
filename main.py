from random import *

randomnum = randint(1, 100)
# print(randomnum)
print("Welcome to number guessing game.")
level = input("Please choose difficulty level 'easy' or 'hard': ")
print(level)

if level == 'easy':
  level = 10
  print(f"You will get {level} chances to find the number!")
if level == 'hard':
  level = 5
  print(f"You will get {level} chances to find the number!")

for i in range(level+1, 0, -1):
  if i > 0:
    num = int(input("Please guess a number: "))
    if num < randomnum:
      print(f"Guess num is bigger than {num}")
    elif num > randomnum:
      print(f"Guess num is smaller than {num}")
    elif num == randomnum:
      print("Woho! you guess the number.")
      break
    chance = i - 2
    if chance == 0:
      print("You lose!")
      break
    print(f"You have more {chance} chances")
    i = i-1
  

# print("You lose!")
  
  