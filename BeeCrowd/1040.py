n1, n2, n3, n4 =  list(map(float, input("Enter multiple values: ").split())) 
'''OR -- n1, n2, n3, n4 = (map(float, input("Enter multiple values: ").split())) '''

media = ((n1*2) + (n2*3) + (n3*4) + n4)/10
print(f'Media: {media:.1f}')

if media >= 7.0:
    print('Aluno aprovado.')
elif media <= 6.9 and media >= 5.0:
    print('Aluno em exame.')
    exame = float(input())
    if (exame + media)/2 >= 5.0:
        print(f'Nota do exame: {exame:.1f}')
        print('Aluno aprovado.')
        print(f'Media final: {((exame + media)/2):.1f}')
    else:
        print('Aluno reprovado.')
        print(f'Media final: {((exame + media)/2):.1f}')
elif media < 5.0:
    print('Aluno reprovado.')
