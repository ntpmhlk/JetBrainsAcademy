# put your python code here
a = int(input())
b = int(input())
total = 0
count = 0
for i in range(a, b + 1):
    if i % 3 == 0:
        total += i
        count += 1
print(total / count)

# Using list concatenation
# a = int(input())
# b = int(input())
# divisible_number = [x for x in range(a, b + 1) if x % 3 == 0]
# print(sum(divisible_number)/len(divisible_number))
