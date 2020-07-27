x = float(input())
y = float(input())

if x > 0:
    if y > 0:
        print('I')
    else:
        print('IV')
elif x < 0:
    if y > 0:
        print('II')
    else:
        print('III')
