import random

list = ["CHALLENGE","COMPARE","COMPANY"]

randomword = random.choice(list).lower()

endofgame = False
lengthofrandomword = len(randomword)
display = []

for _ in range(lengthofrandomword):
  display += "_"
  
while not endofgame:
  guessword = input("Enter a word that you guess: ").lower()
  if guessword in display:
    print("Correct")

  for position in range():