money = int(input())

if money >= 6769:  # sheep
    print(f'{money // 6769} sheep')
elif money >= 3848:  # cow(s)
    print('1 cow' if money // 3848 == 1 else f'{money // 3848} cows')
elif money >= 1296:  # pig(s)
    print('1 pig' if money // 1296 == 1 else f'{money // 1296} pigs')
elif money >= 678:  # goat(s)
    print('1 goat' if money // 678 == 1 else f'{money // 678} goats')
elif money >= 23:  # chicken(s)
    print('1 chicken' if money // 23 == 1 else f'{money // 23} chickens')
else:
    print('None')
