m = {'january': 31, 'february': 28, 'march': 31, 'april': 30, 'may': 31, 'june': 30, 'july': 31, 'august': 31, 'september': 30, 'october': 31, 'november': 30, 'december': 31}
month = (input('Input month '))
day = int(input('Input day '))
if month in m and 0 < m.get(month) >= int(day):
    print(True)
else:
    print(False)