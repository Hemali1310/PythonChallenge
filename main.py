from filedata import data
import random
from replit import clear

def formatdata(randomdata):
  name = randomdata["name"]
  description = randomdata["description"]
  country = randomdata["country"]
  return f"{name}, a {description} from {country}"

score = 0

def checkans(more_follower, follower_a, follower_b):
  if follower_a > follower_b:
    return more_follower == 'A'
  else:
    return more_follower == 'B'
  
def randomteam():
 return random.choice(data)

# print(f"Compare A: {formatdata(random_a)}")
# print(f"Compare B: {formatdata(random_b)}")
# more_follower = input("Who has more follower A or B: ")

# follower_a = random_a["follower_count"]
# follower_b = random_b["follower_count"]
# finalguess = checkans(more_follower, follower_a, follower_b)

def higherlower():
  score = 0
  continuegame = True
  random_a = randomteam()
  random_b = randomteam()

  while continuegame:
    random_a = random_b
    random_b = randomteam()

    while random_a == random_b:
      random_b = randomteam()

    print(f"Compare A: {formatdata(random_a)}.")
    print(f"Compare B: {formatdata(random_b)}.")

    more_follower = input("Who has more follower A or B: ")
    follower_a = random_a["follower_count"]
    follower_b = random_b["follower_count"]
    finalans = checkans(more_follower,follower_a, follower_b)

    clear()

    if finalans:
      score = score + 1
      print(f"Your score is {score}")
    else:
      continuegame = False
      print(f"Your score is {score}")

higherlower()
      


# random_index1 = randint(0, len(data)-1)
# output1 = data[random_index1]['follower_count']
# name1 = data[random_index1]['name']
# description1 = data[random_index1]['description']
# country1 = data[random_index1]['country']
  
# random_index2 = randint(0, len(data)-1)
# output2 = data[random_index2]['follower_count']
# name2 = data[random_index2]['name']
# description2 = data[random_index2]['description']
# country2 = data[random_index2]['country']

# random_index3 = randint(0, len(data)-1)
# output3 = data[random_index3]['follower_count']
# name3 = data[random_index3]['name']
# description3 = data[random_index3]['description']
# country3 = data[random_index3]['country']

# print(f"Compare A: {name1} a {description1} from {country1}")
# print(f"Compare B: {name2} a {description2} from {country2}")

# more_follower = input("Who has more followers A or B: ")
# print(more_follower)
# score = 0 

# def comparison():
#   print(f"Compare A: {name2} a {description2} from {country2}")
#   print(f"Compare B: {name3} a {description3} from {country3}")
#   more_follower = input("Who has more followers A or B: ")

# # def morefollowerA(output1, output2, score, more_follower):
# #   if(more_follower == 'A'):
# #     if(output1 > output2):
# #       score = score + 1
# #       output1 = output2
# #       output2 = output3
# #       comparison()
# #       morefollowerA()



# if(more_follower == 'A'):
#   if(output1 > output2):
#     score = score + 1
#     output1 = output2
#     output2 = output3
#     comparison()
#     morefollowerA()
#     # if(output1 > output2):
#     #   score = score + 1
#     #   print(f"Your score is------- {score}")
#     #   comparison()
#     # else:
#     #   print(f"Your score is,,,,,,,, {score}")
#   else:
#     print(f"Your score is {score}")
# else:
#   if(output2 > output1):
#     score = score + 1
#     output1 = output2
#     output2 = output3
#     comparison()
#     if(output1 > output2):
#       score = score + 1
#       print(f"Your score is====== {score}")
#       comparison()
#     else:
#       print(f"Your score is..... {score}")
#   else:
#     print(f"Your score is/////// {score}")  


# def morefollowerA():
#   if(more_follower == 'A'):
#     if(output1 > output2):
#       score = score + 1
#       output1 = output2
#       output2 = output3
#       print(f"Compare A: {name2} a {description2} from {country2}")
#       print(f"Compare B: {name3} a {description3} from {country3}")
#       more_follower = input("Who has more followers A or B: ")
#       print(more_follower)
#       print(score)
#       morefollowerA()
#     else:
#       print(score)

# if(follower_a > follower_b and guess == follower_a):
  #   score = score + 1
  #   return f"Your score is {score}"
  # elif(follower_a < follower_b and guess == follower_a):
  #   return f"Your score is {score}"
  # elif(follower_a > follower_b and guess == follower_b):
  #   return f"Your score is {score}"
  # elif(follower_a < follower_b and guess == follower_a):
  #   score = score + 1
  #   return f"Your score is {score}"