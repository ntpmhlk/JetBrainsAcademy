ref_time = 10.5
offset_time = int(input())
if ref_time + offset_time < 0:
    print('Monday')
elif ref_time + offset_time > 24:
    print('Wednesday')
else:
    print('Tuesday')
