#Learning / Collatz
    #This program performs a magic trick and can make any number disappear!
def collatz(number):
    if number % 2 == 0:
        print(str(number) + '/2 makes: ', end='')
        return number // 2
    elif number % 2 == 1:
        print(str(number) + '*3+1 is: ', end='')
        return number * 3 + 1

print("Pick a number and I bet I can make it disappear!")

number = int(input())

while number != 1:
    number = collatz(number)
    print(number)

print('And 1 minus 1 equasl…zero!')
print("How'd I do?")