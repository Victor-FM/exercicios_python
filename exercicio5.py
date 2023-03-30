"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

numero_inteiro = input('Digite um numero inteiro: ')
int_numero_inteiro = int(numero_inteiro)
calculo = int_numero_inteiro % 2

if numero_inteiro.isdigit():
    if calculo == 1:
        print('Esse número é ímpar')
    else:
        print('Esse número é par') 
else:
    print('Esse número não é um inteiro')   

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

horario = input('Que horas são: ')

int_horario = int(horario)


if int_horario > 0 and int_horario < 11:
    print('Bom dia')
elif int_horario > 12 and int_horario < 17:
    print('Boa tarde')
elif int_horario > 18 and int_horario < 23:
    print('Boa noite')        

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = input('Digite seu nome: ')

if (len(nome)) <= 4:
    print('Seu nome é curto')
elif (len(nome)) == 5 or (len(nome)) == 6:
    print('Seu nome é normal')
elif (len(nome)) > 6:
    print('Seu nome é muito grande')
