produtos = []

def cadastrar_produto():
    """Função para cadastrar um novo produto."""
    print('\n==== Cadastrar Produto ====')
    nome = input('Nome do produto: ').strip()
    while not nome:
        print('Nome não pode ser vazio. Tente novamente.')
        nome = input('Nome do produto: ').strip()
    while True:
        try:
            preco = float(input('Preço do produto: R$ '))
            if preco < 0:
                print('Preço não pode ser negativo.')
            else:
                break
        except ValueError:
            print('Por favor, digite um valor numérico para o preço.')

    while True:
        try:
            estoque = int(input('Quantidade em estoque: '))
            if estoque < 0:
                print('Quantidade não pode ser negativa.')
            else:
                break
        except ValueError:
            print('Por favor, digite um número inteiro para a quantidade.')

    produto = {
        'nome': nome,
        'preco': preco,
        'estoque': estoque
    }
    produtos.append(produto)
    print(f"Produto '{nome}' cadastrado com sucesso!")

def listar_produtos():
    """Função para listar todos os produtos cadastrados."""
    print('\n==== Lista de Produtos ====')
    if not produtos:
        print('Nenhum produto cadastrado.')
    else:
        for index, produto in enumerate(produtos):
            nome = produto['nome']
            preco = produto['preco']
            estoque = produto['estoque']
            print(f"{index+1}. Nome: {nome}, Preço: R$ {preco:.2f}, Estoque: {estoque}")

def atualizar_produto():
    """Função para atualizar dados de um produto existente."""
    print('\n==== Atualizar Produto ====')
    if not produtos:
        print('Nenhum produto cadastrado para atualizar.')
        return

    listar_produtos()
    try:
        escolha = int(input('Digite o número do produto que deseja atualizar: '))
        if 1 <= escolha <= len(produtos):
            produto = produtos[escolha - 1]
        else:
            print('Número inválido. Retornando ao menu principal.')
            return
    except ValueError:
        print('Entrada inválida. Retornando ao menu principal.')
        return
        
    print(f"Atualizando produto: {produto['nome']}")
    novo_nome = input('Novo nome (deixe vazio para manter atual): ').strip()
    if novo_nome:
        produto['nome'] = novo_nome
    while True:
        novo_preco = input('Novo preço (deixe vazio para manter atual): R$ ').strip()
        if novo_preco == '':
            break
        try:
            novo_preco_val = float(novo_preco)
            if novo_preco_val < 0:
                print('Preço não pode ser negativo.')
            else:
                produto['preco'] = novo_preco_val
                break
        except ValueError:
            print('Por favor, digite um valor numérico para o preço.')
e
    while True:
        novo_estoque = input('Novo estoque (deixe vazio para manter atual): ').strip()
        if novo_estoque == '':
            break
        try:
            novo_estoque_val = int(novo_estoque)
            if novo_estoque_val < 0:
                print('Estoque não pode ser negativo.')
            else:
                produto['estoque'] = novo_estoque_val
                break
        except ValueError:
            print('Por favor, digite um número inteiro para o estoque.')

    print('Produto atualizado com sucesso!')

def remover_produto():
    """Função para remover um produto da lista."""
    print('\n==== Remover Produto ====')
    if not produtos:
        print('Nenhum produto cadastrado para remover.')
        return

    listar_produtos()
    try:
        escolha = int(input('Digite o número do produto que deseja remover: '))
        if 1 <= escolha <= len(produtos):
            produto = produtos.pop(escolha - 1)
            print(f"Produto '{produto['nome']}' removido com sucesso!")
        else:
            print('Número inválido. Nenhum produto removido.')
    except ValueError:
        print('Entrada inválida. Nenhum produto removido.')

def gerar_relatorio():
    """Função para gerar relatório de produtos."""
    print('\n==== Relatório de Produtos ====')
    if not produtos:
        print('Nenhum produto cadastrado para gerar relatório.')
        return

    total_valor = 0
    total_itens = 0
    for produto in produtos:
        total_valor += produto['preco'] * produto['estoque']
        total_itens += produto['estoque']
    print(f"Quantidade de produtos cadastrados: {len(produtos)}")
    print(f"Quantidade total de itens em estoque: {total_itens}")
    print(f"Valor total em estoque: R$ {total_valor:.2f}")

def main():
    """Função principal que exibe o menu e recebe a opção do usuário."""
    while True:
        print('\n=== Sistema de Produtos ===')
        print('1. Cadastrar produto')
        print('2. Listar produtos')
        print('3. Atualizar produto')
        print('4. Remover produto')
        print('5. Gerar relatório')
        print('6. Sair')
        opcao = input('Escolha uma opção: ')
        
        if opcao == '1':
            cadastrar_produto()
        elif opcao == '2':
            listar_produtos()
        elif opcao == '3':
            atualizar_produto()
        elif opcao == '4':
            remover_produto()
        elif opcao == '5':
            gerar_relatorio()
        elif opcao == '6':
            print('Saindo do sistema. Até logo!')
            break
        else:
            print('Opção inválida. Digite um número de 1 a 6.')

if __name__ == '__main__':
    main()
