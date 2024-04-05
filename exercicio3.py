# Mensagem de boas vindas  
print('-------------------------------------------------------------------')
print('Seja bem-vindo(a) à loja Jordane Padilha xxxxxxxxxxxxx!')
print('-------------------------------------------------------------------')

# Serviço
def escolha_servico():
    while True:
        servico = input("Digite o serviço desejado (DIG para Digitalização, ICO para Impressão Colorida, IBO para Impressão Preto e Branco, FOT para Fotocópia): ").upper()
        if servico in ['DIG', 'ICO', 'IBO', 'FOT']:
            if servico == 'DIG':
                return 1.10
            elif servico == 'ICO':
                return 1.00
            elif servico == 'IBO':
                return 0.40
            elif servico == 'FOT':
                return 0.20
        else:
            print("Opção de serviço inválida. Por favor, tente novamente.")

# Num paginas e desconto
def num_paginas():
    while True:
        try:
            num_paginas = int(input("Digite o número de páginas: "))
            if num_paginas < 20:
                return num_paginas
            elif num_paginas >= 20 and num_paginas < 200:
                return num_paginas * 0.85
            elif num_paginas >= 200 and num_paginas < 2000:
                return num_paginas * 0.80
            elif num_paginas >= 2000 and num_paginas < 20000:
                return num_paginas * 0.75
            else:
                print("Não aceitamos pedidos com mais de 20.000 páginas.")
        except ValueError:
            print("Por favor, digite um valor numérico válido.")

# Extra (encadernação)

def servico_extra():
    while True:
        extra = input("Escolha o serviço adicional (digite 1, 2 ou 0 para continuar):\n1 para encadernação simples\n2 para encadernação de capa dura\n0 se não quiser nenhum adicional: ")

        if extra in ['1', '2', '0']:
            if extra == '1':
                return 15.00
            elif extra == '2':
                return 40.00
            else:
                return 0.00
        else:
            print("Opção de serviço adicional inválida. Por favor, tente novamente.")


# Chamando as funções e calculando o total a pagar
servico = escolha_servico()
num_pags = num_paginas()
extra = servico_extra()

total = (servico * num_pags) + extra

print(f"O total a pagar é: R${total:.2f}")

