number = float(input())
digits = int(input())

print(f'{number:.{digits}f}')  # f-string
# print('{0:.{1}f}'.format(number, digits))  # str.format()
