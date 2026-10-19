materiais = {
    "mouse": 10,
    "teclado": 6,
    "cabo": 20
}

nome = input("Qual material deseja retirar? ").strip().lower()

try:
    quantidade = int(input("Quantas unidades? "))

    if nome not in materiais:
        print("Material não encontrado!")
    elif quantidade <= 0:
        print("A quantidade deve ser maior que zero!")
    elif quantidade > materiais[nome]:
        print(f"Estoque insuficiente! Só existem {materiais[nome]} unidades de {nome}.")
    else:
        materiais[nome] = materiais[nome] - quantidade
        print("Retirada realizada com sucesso!")

    print("\nEstoque atualizado:")
    for material, qtd in materiais.items():
        print(f"- {material}: {qtd}")
except ValueError:
    print("Digite uma quantidade numérica válida!")
