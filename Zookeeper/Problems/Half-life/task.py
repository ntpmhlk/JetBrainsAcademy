N = int(input())
R = int(input())

i = 0
while N >= R:
    N //= 2
    i += 1
print(i * 12)