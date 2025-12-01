# projeto-final-python-Joao-Victor-Cunha-Luiz-Eduardo

Sistema CRUD de Produtos
Descrição do sistema

O Sistema CRUD de Produtos é um programa em Python que funciona no terminal e permite gerenciar produtos de forma simples. Foi desenvolvido como projeto final de Programação I (nível iniciante). Com ele, o usuário consegue cadastrar novos produtos, listar os produtos cadastrados, atualizar dados de um produto existente, remover produtos e gerar um relatório de estoque. Todas essas ações são realizadas através de um menu interativo no terminal.

Funcionalidades

Cadastrar produto: Adiciona um novo produto ao sistema, informando nome, preço e quantidade em estoque.

Listar produtos: Mostra todos os produtos cadastrados com seus dados (nome, preço e estoque).

Atualizar produto: Permite alterar as informações de um produto já cadastrado (por exemplo, mudar o preço ou a quantidade em estoque).

Remover produto: Exclui um produto da lista, removendo-o do sistema.

Gerar relatório: Exibe no terminal um relatório simples com todos os produtos e suas informações.

Sair do programa: Encerra a execução do sistema.

Estrutura dos dados

O sistema usa uma lista de dicionários para armazenar os dados dos produtos. Cada dicionário representa um produto e tem as chaves:

nome (str): Nome do produto.

preco (float): Preço unitário do produto.

estoque (int): Quantidade disponível em estoque.

Por exemplo, um produto pode ser representado assim:

produto = {"nome": "Caneta", "preco": 1.50, "estoque": 100}


Essa estrutura facilita o gerenciamento dos produtos dentro da lista.

Como executar o programa

Certifique-se de ter o Python 3 instalado no seu computador.

Abra o terminal ou prompt de comando.

Navegue até o diretório onde o arquivo Python do sistema está salvo.

Execute o programa com o comando:

python3 sistema_crud.py


O menu do sistema será exibido no terminal. Basta digitar o número da opção desejada e pressionar Enter para realizar cada operação.

Exemplo de uso

A seguir, é mostrado um exemplo de execução do sistema, incluindo o menu principal e o cadastramento de um produto:

===== Sistema CRUD de Produtos =====
1. Cadastrar produto
2. Listar produtos
3. Atualizar produto
4. Remover produto
5. Gerar relatório
6. Sair do programa
Escolha uma opção: 1

Digite o nome do produto: Caneta
Digite o preço do produto: 1.50
Digite a quantidade em estoque: 100
Produto cadastrado com sucesso!

Escolha uma opção: 2

Produtos cadastrados:
- Caneta: R$1.50 (Estoque: 100)

Tecnologias utilizadas

Python 3

Terminal / Prompt de Comando

Autores

Aluno 1 - Nome

Aluno 2 - Nome
