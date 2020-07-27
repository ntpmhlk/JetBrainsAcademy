income = int(input())

if income <= 15527:
    percent = 0
elif income <= 42707:
    percent = 15
elif income <= 132406:
    percent = 25
else:
    percent = 28

calculated_tax = round(income * percent / 100)
print(f'The tax for {income} is {percent}%. That is {calculated_tax} dollars!')  # f-string
# print('The tax for {} is {}%. That is {} dollars!'.format(income, percent, calculated_tax))  # str.format()
