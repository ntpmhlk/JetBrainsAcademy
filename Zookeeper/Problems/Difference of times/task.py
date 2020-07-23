# put your python code here
time_1 = [int(input()), int(input()), int(input())]
time_2 = [int(input()), int(input()), int(input())]
time_1_second = time_1[0] * 60 * 60 + time_1[1] * 60 + time_1[2]
time_2_second = time_2[0] * 60 * 60 + time_2[1] * 60 + time_2[2]
print(time_2_second - time_1_second)