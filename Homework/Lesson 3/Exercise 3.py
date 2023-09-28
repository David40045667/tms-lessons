x = int(input('Enter the amount '))
y = int(input('Enter number of years '))
for a in range(y):
    x = int(x+10*x/100)
print(x)