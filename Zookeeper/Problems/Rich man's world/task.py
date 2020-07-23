deposit = int(input())
interest = 7.1
year = 0

while deposit < 700000:
    deposit = deposit * ((100 + interest) / 100)
    year += 1
print(year)
