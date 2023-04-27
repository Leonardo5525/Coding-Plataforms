n = int(input())

minutos = n // 60
segundos = n - minutos * 60
horas = minutos // 60
minutos = minutos -  horas*60

print(f'{horas}:{minutos}:{segundos}')