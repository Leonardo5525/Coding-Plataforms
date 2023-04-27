dinheiro = float(input())

cem = dinheiro//100
dinheiro = dinheiro - cem*100
cin = dinheiro // 50
dinheiro = dinheiro - cin*50
vinte = dinheiro//20
dinheiro = dinheiro - vinte*20
dez = dinheiro//10
dinheiro = dinheiro - dez*10
cinco = dinheiro//5
dinheiro = dinheiro - cinco*5
dois = dinheiro//2
dinheiro = dinheiro - dois*2
um = dinheiro // 1
dinheiro = dinheiro - um*1
p50 = dinheiro//0.50
dinheiro = dinheiro - p50*0.50
p25 = dinheiro//0.25
dinheiro = dinheiro - p25*0.25
p10 = dinheiro//0.10
dinheiro = dinheiro - p10*0.10
p05 = dinheiro // 0.05
dinheiro = dinheiro - p05*0.05
p01 = dinheiro//0.01

	
print('NOTAS:')
print(f'{cem} nota(s) de R$ 100.00')
print(f'{cin} nota(s) de R$ 50.00')
print(f'{vinte} nota(s) de R$ 20.00')
print(f'{dez} nota(s) de R$ 10.00')
print(f'{cinco} nota(s) de R$ 5.00')
print(f'{dois} nota(s) de R$ 2.00')

print('MOEDAS:')
print(f'{um} moeda(s) de R$ 1.00')
print(f'{p50} moeda(s) de R$ 0.50')
print(f'{p25} moeda(s) de R$ 0.25')
print(f'{p10} moeda(s) de R$ 0.10')
print(f'{p05} moeda(s) de R$ 0.05')
print(f'{p01} moeda(s) de R$ 0.01')