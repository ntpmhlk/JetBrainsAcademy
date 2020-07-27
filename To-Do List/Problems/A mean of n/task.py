n = int(input())
total = 0
for _ in range(n):
    total += int(input())
print(total / n)

# Solution by Nino
# n = int(input())
# print(sum(float(input()) for _ in range(n)) / n)
