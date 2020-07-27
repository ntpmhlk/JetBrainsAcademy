n = int(input())
for _ in range(n):
    number = int(input())
    if number % 7 == 0:
        print(number ** 2)

# n = int(input())
# number = []
# for _ in range(n):
#     number.append(int(input()))
# number = [x ** 2 for x in number if x % 7 == 0]
#
# for i in number:
#     print(i)
