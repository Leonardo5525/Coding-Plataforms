x, y = (map(float, input().split())) 

if x == 0 and y == 0:
    print('Origem')
elif x >= 0 and y >= 0:
    print('Q1')
elif x >= 0 and y <= 0:
    print('Q4')
elif x <= 0 and y <= 0:
    print('Q3')
else:
    print('Q2')    