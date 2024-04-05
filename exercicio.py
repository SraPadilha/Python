# Mensagem de boas vindas  
print('-------------------------------------------------------------------')
print('Seja bem-vindo(a) à loja Jordane Padilha xxxxxxxx!')
print('-------------------------------------------------------------------')

# Input do valor unitário e quantidade do produto
valorUnit = float(input('Informe o valor unitário do produto R$:'))
quantidade = float(input('Informe a quantidade: '))

# Cálculo do valor total sem desconto
valorTotalSemDesconto = valorUnit * quantidade

# Verificando e aplicando o desconto 
if valorTotalSemDesconto < 2500.00:
    desconto = 0
elif valorTotalSemDesconto < 6000.00:
    desconto = 4
elif valorTotalSemDesconto < 10000.00:
    desconto = 7
else:
    desconto = 11

# Calculando o valor total com desconto
valorTotalComDesconto = valorTotalSemDesconto * (1 - desconto/100)

# Imprimindo os resultados
print('O valor total sem desconto é de: R$ {:.2f}'.format(valorTotalSemDesconto))

if desconto > 0:
    print('O valor total com desconto é de: R$ {:.2f} ({}% de desconto)'.format(valorTotalComDesconto, desconto))
else:
    print('Nenhum desconto disponível')
print('-------------------------------------------------------------------')


