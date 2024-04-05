
> Questão 1: Imagina-se que você é um dos programadores responsáveis pela construção de app de vendas para uma determinada empresa X que vende em atacado. Uma das estratégias de vendas dessa empresa X é dar desconto maiores conforme o valor total da compra conforme a seguinte listagem:

1.	Se valor total da compra for menor que R$ 2500.00 o desconto será de 0%;
2. Se valor total da compra for igual ou maior que R$ 2500.00 e menor que R$ 6000.00 o desconto será de 4%;
3. Se valor total da compra for igual ou maior que R$ 6000.00 e menor que R$ 10000.00 o desconto será de 7%;
4. Se valor total da compra for igual ou maior que R$ 10000.00 o desconto será de 11%;

Elabore um programa em Python que:

- [X]	Deve-se implementar o print com uma mensagem de boas-vindas que apareça o seu nome [EXIGÊNCIA DE CÓDIGO 1 de 6];
- [X] Deve-se implementar o input do valor unitário e da quantidade do produto [EXIGÊNCIA DE CÓDIGO 2 de 6];
- [X] Deve-se implementar o desconto conforme a enunciado acima (obs.: atente-se as condições de menor, igual e maior) [EXIGÊNCIA DE CÓDIGO 3 de 6];
- [X] Deve-se implementar o valor total sem desconto e o valor total com desconto [EXIGÊNCIA DE CÓDIGO 4 de 6];
- [X] Deve-se implementar as estruturas if, elif e else (todas elas) [EXIGÊNCIA DE CÓDIGO 5 de 6];  
- [X] Deve-se inserir comentários relevantes no código [EXIGÊNCIA DE CÓDIGO 6 de 6];
- [X] Deve-se apresentar na saída de console uma mensagem de boas-vindas com seu nome [EXIGÊNCIA DE SAÍDA DE CONSOLE 1 de 2];
- [X] Deve-se apresentar na saída de console um pedido recebendo desconto (valor total sem desconto acima de R$ 2500.00) [EXIGÊNCIA DE SAÍDA DE CONSOLE 2 de 2];

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

> Questão 2: Você e sua equipe de programadores foram contratados para desenvolver um app de vendas para uma loja que vende Açaí e Cupuaçu. Você ficou com a parte de desenvolver a interface do cliente para retirada do produto.
A Loja possui seguinte relação:

1. Tamanho P de Cupuaçu (CP) custa R$ 9.00 e o Açaí (AC) custa R$ 11.00;
2. Tamanho M de Cupuaçu (CP) custa R$ 14.00 e o Açaí (AC) custa R$ 16.00;
3. Tamanho G de Cupuaçu (CP) custa R$ 18.00 e o Açaí (AC) custa R$ 20.00;
4.  	
Elabore um programa em Python que: 
 
- [X] 	Deve-se implementar o print com uma mensagem de boas-vindas que apareça o seu nome [EXIGÊNCIA DE CÓDIGO 1 de 8];
- [X] 	Deve-se implementar o input  do sabor (CP/AC) e o print “Sabor inválido. Tente novamente" se o usuário entrar com valor diferente de CP e AC [EXIGÊNCIA DE CÓDIGO 2 de 8];
- [X] 	Deve-se implementar o input  do tamanho (P/M/G) e o print “Tamanho inválido. Tente novamente" se o usuário com entra valor diferente de P,M ou G [EXIGÊNCIA DE CÓDIGO 3 de 8];
- [X] 	Deve-se implementar if/elif com cada uma das combinações de sabor e tamanho do enunciado [EXIGÊNCIA DE CÓDIGO 4 de 8];
- [X] 	Deve-se implementar um acumulador para somar os valores dos pedidos [EXIGÊNCIA DE CÓDIGO 5 de 8];
- [X] 	Deve-se implementar o input com a pergunta: “Deseja pedir mais alguma coisa?”. Se sim repetir a partir do item B, senão encerrar o programa executar o print do acumulador [EXIGÊNCIA DE CÓDIGO 6 de 8];
- [X] 	Deve-se implementar as estruturas de while, break, continue (todas elas) [EXIGÊNCIA DE CÓDIGO 7 de 8];
- [ ] 	Deve-se inserir comentários relevantes no código [EXIGÊNCIA DE CÓDIGO 8 de 8];
- [X] 	Deve-se apresentar na saída de console uma mensagem de boas-vindas com o seu nome [EXIGÊNCIA DE SAÍDA DE CONSOLE 1 de 4];
- [X] 	Deve-se apresentar na saída de console um pedido em que o usuário errou o sabor [EXIGÊNCIA DE SAÍDA DE CONSOLE 2 de 4]; 
- [X] 	Deve-se apresentar na saída de console um pedido em que o usuário errou o tamanho [EXIGÊNCIA DE SAÍDA DE CONSOLE 3 de 4];
- [X] 	Deve-se apresentar na saída de console um pedido com duas opções sabores diferentes e com tamanhos diferentes [EXIGÊNCIA DE SAÍDA DE CONSOLE 4 de 4];

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

> Questão 3: Você foi contratado para desenvolver um sistema de cobrança de serviços de uma copiadora. Você ficou com a parte de desenvolver a interface com o funcionário.
A copiadora opera da seguinte maneira:

1. Serviço de Digitalização (DIG) o custo por página é de um real e dez centavos;
2. Serviço de Impressão Colorida (ICO) o custo por página é de um real; 
3. Serviço de Impressão Preto e Branco (IBO) o custo por página é de quarenta centavos;
4. Serviço de Fotocópia (FOT) o custo por página é de vinte centavos;
5. Se número de páginas for menor que 20 retornar o número de página sem desconto;
6. Se número de páginas for igual ou maior que 20 e menor que 200 retornar o número de páginas com o desconto é de 15%;
7. Se número de páginas for igual ou maior que 200 e menor que 2000 retornar o número de páginas com o desconto é de 20%;
8. Se número de páginas for igual ou maior que 2000 e menor que 20000 retornar o número de páginas com o desconto é de 25%;
9. Se número de páginas for maior ou igual à 20000 não é aceito pedidos nessa quantidade de páginas;

- Para o adicional de encadernação simples (1) é cobrado um valor extra de 15 reais;
- Para o adicional de encadernação de capa dura (2) é cobrado um valor extra de 40 reais;
- Para o adicional de não querer mais nada (0) é cobrado um valor extra de 0 reais;


   O valor final da conta é calculado da seguinte maneira:
  
      total = servico * num_pagina + extra

 
Elabore um programa em Python que: 
 
- [X] 	Deve-se implementar o print com uma mensagem de boas-vindas que apareça o seu nome [EXIGÊNCIA DE CÓDIGO 1 de 7];
- [X] 	Deve-se implementar a função escolha_servico() em que: [EXIGÊNCIA DE CÓDIGO 2 de 7];
- [X] 	Pergunta o servico desejado;
- [X]   Retorna o valor do serviço com base na escolha do usuário;
- [X] 	Repete a pergunta do item B.a se digitar serviço se digitar uma opção diferente de: dig/ico/ibo/fot;
- [X] 	Deve-se implementar a função num_pagina() em que: [EXIGÊNCIA DE CÓDIGO 3 de 7];
- [X] 	Pergunta o número de páginas;
- [X] 	Retorna o número de páginas com desconto seguindo a regra do enunciado;
- [X] 	Repete a pergunta do item C.a se digitar um valor acima de 20000 ou valor não numérico (use try/except para não numérico)
- [X] 	Deve-se implementar a função servico_extra() em que: [EXIGÊNCIA DE CÓDIGO 4 de 7];
- [X] 	Pergunta pelo serviço adicional;
- [X] 	Retornar uma das opções de adicional 
- [X] 	Repetir a pergunta item D.a se digitar uma opção diferente de: 1/2/0;
- [X] 	Deve-se implementar o total a pagar na parte do main conforme o enunciado [EXIGÊNCIA DE CÓDIGO 5 de 7];
- [X] 	Deve-se implementar try/except [EXIGÊNCIA DE CÓDIGO 6 de 7];
- [X] 	Deve-se inserir comentários relevantes no código [EXIGÊNCIA DE CÓDIGO 7 de 7];
- [X] 	Deve-se apresentar na saída de console uma mensagem de boas-vindas com o seu nome [EXIGÊNCIA DE SAÍDA DE CONSOLE 1 de 4];
- [X] 	Deve-se apresentar na saída de console um pedido no qual o usuário errou a opção de serviço [EXIGÊNCIA DE SAÍDA DE CONSOLE 2 de 4];
- [X]   Deve-se apresentar na saída de console um pedido no qual o usuário digitou ultrapassou no número de páginas [EXIGÊNCIA DE SAÍDA DE CONSOLE 3 de 4];
- [X] 	Deve-se apresentar na saída de console um pedido com opção de serviço, número de páginas e serviço extra válidos [EXIGÊNCIA DE SAÍDA DE CONSOLE 4 de 4];

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

> Questão 4: Você e sua equipe de programadores foram contratados por pequena empresa para desenvolver o software de gerenciamento de pessoas. Este software deve ter o seguinte menu e opções:

1.	Cadastrar Livro
2.	Consultar Livro
3.	Consultar Todos 
4.	Consultar por Id
5.	Consultar por Autor
6.	Retornar ao menu
7.	Remover Livro
8.	Encerrar Programa

Elabore um programa em Python que: 
 
- [X]	Deve-se implementar o print com uma mensagem de boas-vindas que apareça o seu nome [EXIGÊNCIA DE CÓDIGO 1 de 8];
- [X]	Deve-se implementar uma lista vazia com o nome de lista_livro e a variável id_global com valor inicial igual a 0 [EXIGÊNCIA DE CÓDIGO 2 de 8];
- [X]	Deve-se implementar uma função chamada cadastrar_livro(id) em que: [EXIGÊNCIA DE CÓDIGO 3 de 8];
- [X]	Pergunta nome, autor, editora do livro;
- [X]	Armazena o id (este é fornecido via parâmetro da função), nome, autor, editora dentro de um dicionário;
- [X]	Copiar o dicionário para dentro da lista_livro;
- [X]	Deve-se implementar uma função chamada consultar_livro() em que: [EXIGÊNCIA DE CÓDIGO 4 de 8];
- [X]	Deve-se perguntar qual opção deseja (1. Consultar Todos / 2. Consultar por Id / 3. Consultar por Autor / 4. Retornar ao menu) e   printar a “Opção inválida" se entrar com valor diferente de 1, 2, 3 ou 4 :
- [X]	Se Consultar Todos, apresentar todos os livros com todos os seus dados cadastrados;
- [X]	Se Consultar por Id, apresentar o livro específico com todos os seus dados cadastrados;
- [X]	Se Consultar por Autor, apresentar o(s) livro(s) do autor com todos os seus dados cadastrados;
- [X]	Se Retornar ao menu, deve-se retornar ao menu principal;
- [X]	Deve-se implementar uma função chamada remover_livro() em que: [EXIGÊNCIA DE CÓDIGO 5 de 8];
- [X]	Deve-se pergunta pelo id do colaborador a ser removido;
- [X]	Remover o livro da lista_livro;
- [X]	Deve-se implementar uma estrutura de menu no main em que: [EXIGÊNCIA DE CÓDIGO 6 de 8];
- [X]	Deve-se pergunta qual opção deseja (1. Cadastrar Livro / 2. Consultar Livro / 3. Remover Livro / 4. Encerrar Programa)e executar o printar de “Opção inválida" se entrar com valor diferente de 1, 2, 3 ou 4 :
- [X] Se Cadastrar Livro, acrescentar em um id_ global e chamar a função cadastrar_livro(id_ global);
- [X]	Se Consultar Livro, chamar função consultar_livro();
- [X]	Se Remover Livro, chamar função remover_livro();
- [X]	Se Encerrar Programa, sair do menu (e com isso acabar a execução do código);
- [X]	Deve-se implementar uma lista de dicionários (uma lista contento dicionários dentro) [EXIGÊNCIA DE CÓDIGO 7 de 8];
- [X]	Deve-se inserir comentários relevantes no código [EXIGÊNCIA DE CÓDIGO 8 de 8];
- [X]	Deve-se apresentar na saída de console uma mensagem de boas-vindas com o seu nome [EXIGÊNCIA DE SAÍDA DE CONSOLE 1 de 6];
- [X]	Deve-se apresentar na saída de console um cadastro de 3 livros (sendo 2 deles no mesmo autor) [EXIGÊNCIA DE SAÍDA DE CONSOLE 2 de 6];
- [X]	Deve-se apresentar na saída de console uma consulta de todos os livros [EXIGÊNCIA DE SAÍDA DE CONSOLE 3 de 6];
- [X]	Deve-se apresentar na saída de console uma consulta por código de um dos livros [EXIGÊNCIA DE SAÍDA DE CONSOLE 4 de 6];
- [X]	Deve-se apresentar na saída de console uma consulta por setor em que 2 livros sejam do mesmo autor [EXIGÊNCIA DE SAÍDA DE CONSOLE 5 de 6];
- [X]	Deve-se apresentar na saída de console uma remoção de um dos livros seguida de uma consulta de todos os livros [EXIGÊNCIA DE SAÍDA DE CONSOLE 6 de 6];



-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

 Nota adicional[^1].

Foot note[^2].

[^1]: A questão 4 está com bastante errinhos em comparação as outras, mas ainda cumpre os requisitos básicos do exercício.
[^2]: Foi um trabalho da faculdade que já está corrigido, vou deixar aqui do jeito que enviei, fiquei com a nota final de 83.














