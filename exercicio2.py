# Mensagem de boas vindas  
print('--------------------------------------------------------------------------')
print('Seja bem-vindo(a) à loja Jordane Padilha 4665714!')
print('--------------------------------------------------------------------------')

print("Cardápio")
print("-" * 49)
print("| Sabor \t| Tamanho\t| preço \t|")
print("-" * 49)
print("| Cupuaçu \t| P\t\t| 9.00 \t\t|")
print("-" * 49)
print("| Cupuaçu \t| M\t\t| 14.00\t\t|")
print("-" * 49)
print("| Cupuaçu \t| G\t\t| 18.00\t\t|")
print("-" * 49) 
print("| Açaí \t\t| P\t\t| 11.00 \t\t|")
print("-" * 49)
print("| Açaí \t\t| M\t\t| 16.00\t\t|")
print("-" * 49) 
print("| Açaí  \t| G\t\t| 20.00\t\t|")
print("-" * 49)


acumulador = 0

while True:
    sabor = input('Digite o sabor (CP para Cupuaçu ou AC para Açaí): ')
    if sabor not in ['CP', 'AC']:
        print('Sabor inválido. Tente novamente.')
        continue
    
    tamanho = input('Digite o tamanho (P, M ou G): ')
    if tamanho not in ['P', 'M', 'G']:
        print('Tamanho inválido. Tente novamente.')
        continue
    
    if sabor == 'CP' and tamanho == 'P':
        acumulador += 9.00
    elif sabor == 'AC' and tamanho == 'P':
        acumulador += 11.00
    elif sabor == 'CP' and tamanho == 'M':
        acumulador += 14.00
    elif sabor == 'AC' and tamanho == 'M':
        acumulador += 16.00
    elif sabor == 'CP' and tamanho == 'G':
        acumulador += 18.00
    elif sabor == 'AC' and tamanho == 'G':
        acumulador += 20.00
    
    mais_pedidos = input('Deseja pedir mais alguma coisa? (S/N): ')
    if mais_pedidos.upper() != 'S':
        break

# Exigência de saída de console
print(f"Total do pedido: R$ {acumulador:.2f}")


print('--------------------------------------------------------------------------')
