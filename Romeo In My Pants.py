#This short program based on one of the lessons on py4e.org downloads the full text of
#Romeo & Juliet and randomly adds "in my pants" to the end of each line
import urllib.request, random

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo-full.txt')
print(" ")
for line in fhand:
    print(line.decode().strip() + ' in my pants' * random.randint(0,1))
print(" ")