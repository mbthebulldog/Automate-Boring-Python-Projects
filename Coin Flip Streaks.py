import random, re
from sre_constants import RANGE

streakNum = 0

for experimentNum in range(10000):
    #Create a list of 100 heads (1) or tails (0) values
    list = []

    for flip in range(100):
        list.append(str(random.randint(0, 1)))

    #Check if a streak of 6 heads or 6 tails in a row
    list = ''.join(list)
    streaks = re.findall('0{6}|1{6}', str(list))
    streakNum = streakNum + len(streaks)
    
    #Debugging
    #print(list)
    #print(streaks)
    #print(streakNum)
    
print('Number of streaks in 10,000 experiments: ' + str(streakNum))
print('Chance of streak is ' + str(streakNum / 10000))