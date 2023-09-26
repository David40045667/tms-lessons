sum = 0
for i in range(101):
    sum += i
print(f'1: {sum}')


sum = 0
for i in range(100, 1001):
    sum += i
print(f'2: {sum}')


sum = 0
for i in range(100, 1001, 2):
    sum += i
print(f'3: {sum}')


sum = 1
for i in range(1, 11):
    sum *= i
print(f'4: {sum}')


sum = 2
for i in range(1, 10):
    sum *= 2
print(f'5: {sum}')


summ = 0
for i in range(1000):
    summ += i
    if summ > 1000:
        break
print(f'6: {summ} {i}')



