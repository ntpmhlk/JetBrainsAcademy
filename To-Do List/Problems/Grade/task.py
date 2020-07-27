student_score = int(input())
max_score = int(input())

if student_score < 0.6 * max_score:
    print('F')
elif student_score < 0.7 * max_score:
    print('D')
elif student_score < 0.8 * max_score:
    print('C')
elif student_score < 0.9 * max_score:
    print('B')
else:
    print('A')
