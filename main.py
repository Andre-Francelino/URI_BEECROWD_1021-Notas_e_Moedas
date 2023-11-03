#URI 1021 - Notas e Moedas

#Entrada - Ler valor de ponto flutuante
vlr = round(float(input()), 2)

#Calculando o menor número de cédulas possíveis (notas consideradas: 100, 50, 20, 10, 5, 2 e 1)
cedula_100 = vlr // 100
cedula_50 = vlr % 100 // 50
cedula_20 = vlr % 100 % 50 // 20
cedula_10 = vlr % 100 % 50 % 20 // 10
cedula_5 = vlr % 100 % 50 % 20 % 10 // 5
cedula_2 = vlr % 100 % 50 % 20 % 10 % 5 // 2

#Declarando variável RESTANTE para o calculo das moedas
restante = vlr % 100 % 50 % 20 % 10 % 5 % 2

#Calculando o menor número de moedas possíveis (moedas consideradas: 1, 0.50, 0.25, 0.10, 0.05 e 0.01)
moeda_1 = restante // 1
moeda_50 = restante % 1 // 0.50
moeda_25 = restante % 1 % 0.50 // 0.25
moeda_10 = restante % 1 % 0.50 % 0.25 // 0.10
moeda_05 = restante % 1 % 0.50 % 0.25 % 0.10 // 0.05
moeda_01 = restante % 1 % 0.50 % 0.25 % 0.10 % 0.05 / 0.01

#Realizando o método Casting para conversão das varáveis para o tipo INTEIRO
cedula_100 = int(cedula_100)
cedula_50 = int(cedula_50)
cedula_20 = int(cedula_20)
cedula_10 = int(cedula_10)
cedula_5 = int(cedula_5)
cedula_2 = int(cedula_2)
moeda_1 = int(moeda_1)
moeda_50 = int(moeda_50)
moeda_25 = int(moeda_25)
moeda_10 = int(moeda_10)
moeda_05 = int(moeda_05)
moeda_01 = int(moeda_01)

#Impressão de saídas -> quantidades de notas
print('NOTAS:')
print(cedula_100,'nota(s) de R$ 100.00')
print(cedula_50,'nota(s) de R$ 50.00')
print(cedula_20,'nota(s) de R$ 20.00')
print(cedula_10,'nota(s) de R$ 10.00')
print(cedula_5,'nota(s) de R$ 5.00')
print(cedula_2,'nota(s) de R$ 2.00')

#Impressão de saídas -> quantidades de moedas
print('MOEDAS:')
print(moeda_1,'moeda(s) de R$ 1.00')
print(moeda_50,'moeda(s) de R$ 0.50')
print(moeda_25,'moeda(s) de R$ 0.25')
print(moeda_10,'moeda(s) de R$ 0.10')
print(moeda_05,'moeda(s) de R$ 0.05')
print(moeda_01,'moeda(s) de R$ 0.01')

