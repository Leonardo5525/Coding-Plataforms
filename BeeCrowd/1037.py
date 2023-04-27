n = float(input())


if n < 0 or n > 100:
    print('Fora de intervalo')
elif n > 75:
    print('Intervalo (75,100]')
elif n > 50:
    print('Intervalo (50,75]')
elif n > 25:
    print('Intervalo (25,50]')
elif n > 0:
    print('Intervalo [0,25]')

'''import math
A,B,C = map(float,input().split())
D = (B**2)-(4*A*C)
if(D <0 or A==0):
    print("Impossivel calcular")
else:
    D=math.sqrt(D)
    R1 = (-B+D)/(2*A)
    R2 = (-B-D)/(2*A)
    print(f'R1 = {R1:0.5f}\nR2 = {R2:0.5f}')'''