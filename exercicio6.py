# Obtendo valor sem desconto
V = float(input('\nInsira o valor do seu salario: '))

# Obtendo a percentagem de desconto

P = 15
#float(input('Insira a percentagem de desconto: '))

# Calculando o valor descontado
Vd = V * 15/100

# Calculando o valor final com desconto
Vf = V + Vd

# Imprimindo o resultado
print("\n==================================================\n")
print('O salario é de: R$ {:,.2f}'.format(Vf))
#print('O valor a pagar é de: R$ {:,.2f}'.format(Vf))