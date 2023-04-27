d = int(input())

ano = d//365
mes = (d - ano*365)//30
dias = d - (ano*365 + mes*30)

print(f'{ano} ano(s)')
print(f'{mes} mes(es)')
print(f'{dias} dia(s)')
