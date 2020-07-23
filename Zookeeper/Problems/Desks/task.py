# put your python code here
number_student = []
for _ in range(3):
    number_student.append(int(input()))
number_desk = [x // 2 + x % 2 for x in number_student]
print(sum(number_desk))
