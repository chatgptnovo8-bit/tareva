estoque = [
    {"codigo": 101, "nome": "Teclado", "quantidade": 8, "preco": 75.0},
    {"codigo": 102, "nome": "Mouse", "quantidade": 15, "preco": 40.0},
    {"codigo": 103, "nome": "Monitor", "quantidade": 4, "preco": 850.0}
]


def buscar_produto(codigo):
    """Devolve o produto com o código informado ou None."""
    for produto in estoque:
        if produto["codigo"] == codigo:
            return produto
    return None


def cadastrar_produto():
    print("\n--- CADASTRAR PRODUTO ---")

    try:
        codigo = int(input("Código do produto: "))
    except ValueError:
        print("O código deve ser um número inteiro!")
        return

    if buscar_produto(codigo) is not None:
        print("Esse código já existe!")
        return

    nome = input("Nome do produto: ").strip()
    if nome == "":
        print("O nome não pode ficar vazio!")
        return

    try:
        quantidade = int(input("Quantidade inicial: "))
        preco = float(input("Preço unitário: "))
    except ValueError:
        print("Digite valores numéricos válidos!")
        return

    if quantidade < 0 or preco < 0:
        print("Quantidade e preço não podem ser negativos!")
        return

    produto = {
        "codigo": codigo,
        "nome": nome,
        "quantidade": quantidade,
        "preco": preco
    }

    estoque.append(produto)
    print("Produto cadastrado com sucesso!")


def listar_produtos():
    print("\n--- PRODUTOS CADASTRADOS ---")

    if len(estoque) == 0:
        print("Nenhum produto cadastrado.")
        return

    for produto in estoque:
        print(
            "Código:", produto["codigo"],
            "| Nome:", produto["nome"],
            "| Quantidade:", produto["quantidade"],
            "| Preço: R$", f"{produto['preco']:.2f}"
        )


def pesquisar_produto():
    print("\n--- PESQUISAR PRODUTO ---")

    try:
        codigo = int(input("Digite o código: "))
    except ValueError:
        print("O código precisa ser um número!")
        return

    produto = buscar_produto(codigo)
    if produto is not None:
        print("Produto encontrado:", produto["nome"])
        print("Quantidade:", produto["quantidade"])
        print("Preço: R$", f"{produto['preco']:.2f}")
    else:
        print("Produto não encontrado!")


def registrar_entrada():
    print("\n--- ENTRADA DE MERCADORIA ---")
    try:
        codigo = int(input("Código do produto: "))
    except ValueError:
        print("Código inválido!")
        return

    produto = buscar_produto(codigo)
    if produto is None:
        print("Produto não encontrado!")
        return

    try:
        quantidade = int(input("Quantidade recebida: "))
    except ValueError:
        print("A quantidade deve ser um número inteiro!")
        return

    if quantidade <= 0:
        print("A quantidade recebida deve ser maior que zero!")
        return

    produto["quantidade"] = produto["quantidade"] + quantidade
    print("Entrada registrada com sucesso!")


def relatorio_estoque():
    print("\n--- RELATÓRIO DO ESTOQUE ---")
    total_unidades = 0
    valor_total = 0
    for produto in estoque:
        total_unidades = total_unidades + produto["quantidade"]
        valor_total = valor_total + produto["quantidade"] * produto["preco"]
    print("Quantidade total de unidades:", total_unidades)
    print("Valor total do estoque: R$", f"{valor_total:.2f}")


def menu():
    while True:
        print("\n===== SISTEMA DE ESTOQUE =====")
        print("1 - Cadastrar produto")
        print("2 - Listar produtos")
        print("3 - Pesquisar produto")
        print("4 - Registrar entrada")
        print("5 - Relatório de estoque")
        print("6 - Sair")
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            cadastrar_produto()
        elif opcao == "2":
            listar_produtos()
        elif opcao == "3":
            pesquisar_produto()
        elif opcao == "4":
            registrar_entrada()
        elif opcao == "5":
            relatorio_estoque()
        elif opcao == "6":
            print("Encerrando o sistema...")
            break
        else:
            print("Opção inválida!")


menu()
