min_col = 1
max_col = 8
min_row = 1
max_row = 8

king_col = int(input())
king_row = int(input())
move = 0

if king_col > min_col:  # left
    move += 1
if king_col < max_col:  # right
    move += 1
if king_row > min_row:  # down
    move += 1
if king_row < max_row:  # up
    move += 1
if king_col > min_col and king_row > min_row:  # left down
    move += 1
if king_col > min_col and king_row < max_row:  # left up
    move += 1
if king_col < max_col and king_row > min_row:  # right down
    move += 1
if king_col < max_col and king_row < max_row:  # right up
    move += 1

print(move)

'''
# Solution by Anna Khabarova
num1 = int(input())
num2 = int(input())

if num1 in [1, 8] and num2 in [1, 8]:
    print(3)
elif num1 in [8, 1] or num2 in [8, 1]:
    print(5)
else:
    print(8)
'''
