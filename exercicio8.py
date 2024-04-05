# Obtendo valor sem desconto
V = float(input('\nInsira o valor sem desconto do produto: '))

# Obtendo a percentagem de desconto

P = 6
#float(input('Insira a percentagem de desconto: '))

# Calculando o valor descontado
Vd = V * 6/100

# Calculando o valor final com desconto
Vf = V - Vd

# Imprimindo o resultado
print("\n==================================================\n")
print('O valor descontado é de: R$ {:,.2f}'.format(Vd))
print('O valor a pagar é de: R$ {:,.2f}'.format(Vf))