#This program helps you eat a whole cake (or whatever is left of it) by yourself!
import random

cake = random.randint(1,10)

print("You found a cake. Looks like someone else found it first, though; there are only " + str(cake) + " slices left!")

while cake>0:
  print("How many slices of cake would you like to eat?")

  try:
    slices = int(input()) 
  except:
    print("Numbers only, please")
    continue

  if cake >= slices:
    cake -= slices
    print("There are now " + str(cake) + " slices of cake left")
  else:
    print("There's not enough cake left!")

print("Congratulations! You ate the whole thing! #naptime")