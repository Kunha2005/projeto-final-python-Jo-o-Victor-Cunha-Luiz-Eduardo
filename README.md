# projeto-final-python-Joao-Victor-Cunha-Luiz-Eduardo

Sistema CRUD de Produtos
Descrição do sistema
O Sistema CRUD de Produtos é um projeto simples desenvolvido em Python que funciona no terminal. Ele permite ao usuário gerenciar um cadastro de produtos com operações básicas de criar, visualizar, atualizar e remover itens. O programa foi criado como trabalho final da disciplina de Programação I e utiliza uma lista de dicionários para armazenar as informações de cada produto.
Funcionalidades
Cadastrar produto: Adiciona um novo produto ao sistema com nome, preço e quantidade em estoque informados pelo usuário.
Listar produtos: Exibe todos os produtos cadastrados, mostrando nome, preço e estoque de cada um.
Atualizar produto: Permite modificar o nome, preço ou estoque de um produto já cadastrado.
Remover produto: Remove um produto existente do sistema.
Gerar relatório: Exibe informações resumidas, como o número total de produtos cadastrados e o valor total em estoque.
Sair do programa: Encerra a execução do sistema de forma segura.
Estrutura dos dados
Os produtos são armazenados em uma lista de dicionários. Cada dicionário representa um produto com as chaves nome (string), preco (float) e estoque (int). Abaixo está um exemplo de como esses dados podem ser estruturados:
produtos = [
    {"nome": "Caneta", "preco": 1.5, "estoque": 100},
    {"nome": "Caderno", "preco": 10.0, "estoque": 50}
]
Neste exemplo, temos dois produtos cadastrados: uma caneta e um caderno, cada um com preço e quantidade em estoque definidos.
Como executar o programa
Para executar o sistema, siga estas etapas:
Certifique-se de ter o Python 3 instalado em sua máquina.
Clone ou baixe este repositório em seu computador.
Abra o terminal (linha de comando) e navegue até a pasta do projeto.
Execute o programa com o comando python sistema_crud_produtos.py.
O menu principal será exibido no terminal e você poderá escolher as opções desejadas.
Exemplo de uso
A seguir está um exemplo de uso do programa no terminal. O usuário adiciona um produto e depois visualiza a lista de produtos cadastrados:
Bem-vindo ao Sistema CRUD de Produtos!
1. Cadastrar produto
2. Listar produtos
3. Atualizar produto
4. Remover produto
5. Gerar relatório
6. Sair

Escolha uma opção: 1
Nome do produto: Caneta
Preço: 2.50
Quantidade em estoque: 100
Produto cadastrado com sucesso!

1. Cadastrar produto
2. Listar produtos
3. Atualizar produto
4. Remover produto
5. Gerar relatório
6. Sair

Escolha uma opção: 2

--- Lista de Produtos ---
1. Nome: Caneta | Preço: 2.50 | Estoque: 100

Escolha uma opção: 6
Saindo do programa...
Tecnologias utilizadas
Python 3: Linguagem de programação utilizada para desenvolver o sistema.
Ambiente de terminal: Interface em que o programa é executado e interage com o usuário.
Autores
Aluno 1 - Nome Completo
Aluno 2 - Nome Completo


