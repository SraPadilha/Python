# Implementação das funções
def cadastrar_livro():
    nome = input("Digite o nome do livro: ")
    autor = input("Digite o nome do autor: ")
    editora = input("Digite o nome da editora: ")
    global id_global
    id_global += 1
    livro = {'id': id_global, 'nome': nome, 'autor': autor, 'editora': editora}
    lista_livro.append(livro)

def consultar_todos():
    if lista_livro:
        for livro in lista_livro:
            print(livro)
    else:
        print("Não há livros cadastrados.")

def consultar_por_id():
    id_consulta = int(input("Digite o ID do livro que deseja consultar: "))
    for livro in lista_livro:
        if livro['id'] == id_consulta:
            print(livro)
            return
    print("Livro não encontrado.")

def consultar_por_autor():
    autor_consulta = input("Digite o nome do autor que deseja consultar: ")
    encontrados = False
    for livro in lista_livro:
        if livro['autor'].lower() == autor_consulta.lower():
            print(livro)
            encontrados = True
    if not encontrados:
        print("Nenhum livro encontrado para o autor especificado.")

def remover_livro():
    id_remover = int(input("Digite o ID do livro que deseja remover: "))
    for livro in lista_livro:
        if livro['id'] == id_remover:
            lista_livro.remove(livro)
            print("Livro removido com sucesso.")
            return
    print("Livro não encontrado.")

# Inicialização das variáveis
lista_livro = []
id_global = 0

# Estrutura de menu principal
while True:
    print("Bem-vindo ao sistema de gerenciamento de livros Jordane Padilha xxxxxxx!")
    opcao = int(input("Escolha uma opção:\n1. Cadastrar Livro\n2. Consultar Livro\n3. Remover Livro\n4. Encerrar Programa\n"))
    
    if opcao == 1:
        cadastrar_livro()
    elif opcao == 2:
        consulta_opcao = int(input("Escolha uma opção de consulta:\n1. Consultar Todos\n2. Consultar por Id\n3. Consultar por Autor\n4. Retornar ao menu\n"))
        if consulta_opcao == 1:
            consultar_todos()
        elif consulta_opcao == 2:
            consultar_por_id()
        elif consulta_opcao == 3:
            consultar_por_autor()
        elif consulta_opcao != 4:
            print("Opção inválida.")
    elif opcao == 3:
        remover_livro()
    elif opcao == 4:
        break
    else:
        print("Opção inválida.")

# Saída de console conforme as exigências
print("Bem-vindo ao sistema de gerenciamento de livros!")
cadastrar_livro()
cadastrar_livro()
cadastrar_livro()
consultar_todos()
consultar_por_id()
consultar_por_autor()
remover_livro()
consultar_todos()
