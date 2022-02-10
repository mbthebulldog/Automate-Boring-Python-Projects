#Learning / H Names
  #This little program helps my wife remember whcih H names she picked out for me over the years
import random

boners = []

for i in range (0,8):
  print("What shall we name boner #" + str(i + 1) + "? (Or press Enter to give up.)")
  name = input()
  if (name == ''):
    break
  while (not name.startswith('h') and not name.startswith('H')):  
      print("That ain't no H name! Try again!")
      name = input()
  boners.append(name)

print("That's enough! These are your boner names:")
for i in range(len(boners)):
  print("#" + str(i + 1) + ": " + str(boners[i]))