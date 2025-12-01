# projeto-final-python-Joao-Victor-Cunha-Luiz-Eduardo

Sistema CRUD de Produtos

#  Descrição do sistema  
O **Sistema CRUD de Produtos** é um programa simples feito em Python para rodar no terminal.  
Ele permite cadastrar, listar, atualizar e remover produtos, além de gerar um relatório completo do estoque.  
O sistema usa uma lista de dicionários para armazenar os dados — cada produto tem nome, preço e quantidade em estoque.  
Esse projeto pode ser usado como trabalho final da disciplina de Programação I.

---

#  Funcionalidades  

- **Cadastrar produto**: pede nome, preço e quantidade em estoque.  
- **Listar produtos**: exibe todos os produtos cadastrados.  
- **Atualizar produto**: permite mudar nome, preço e/ou estoque de um produto existente.  
- **Remover produto**: excluir um produto da lista.  
- **Gerar relatório**: calcula e mostra o total de itens em estoque e o valor total estimado do estoque.  
- **Sair**: encerra o programa.

---

##  Estrutura dos dados  

Os produtos são armazenados em uma lista chamada `produtos`. Cada produto é um dicionário com as chaves:

- `nome` (string) — nome do produto  
- `preco` (float) — preço unitário do produto  
- `estoque` (int) — quantidade disponível  

Exemplo de produto:

```python
{"nome": "Caneta", "preco": 1.50, "estoque": 100}
 Como executar
Instale o Python 3 no seu computador.

Salve o arquivo sistema_produtos.py na sua pasta de trabalho.

Abra o terminal (Prompt de Comando).

Navegue até a pasta onde está o arquivo.

Rode o comando:

bash
Copiar código
python sistema_produtos.py
O menu será exibido. Digite o número da opção desejada e pressione Enter para executar.

  Exemplo de uso
markdown
Copiar código
===== Sistema CRUD de Produtos =====
1. Cadastrar produto
2. Listar produtos
3. Atualizar produto
4. Remover produto
5. Relatório
6. Sair
Escolha uma opção: 1

Nome do produto: Caneta
Preço do produto (R$): 1.50
Quantidade em estoque: 100
✔ Produto 'Caneta' cadastrado com sucesso!

Escolha uma opção: 2
==== Lista de Produtos ====
1. Nome: Caneta | Preço: R$ 1.50 | Estoque: 100
 Tecnologias utilizadas
Python 3

Terminal / Prompt de Comando

Dupla
Alunos – João victor Cunha / Luiz Eduardo

