estoque = []


def definir_id():
    if not estoque:
        return 1
    return max(produto["id"] for produto in estoque) + 1


def exibir_produto(produto):
    print("------------")
    print("ID:", produto["id"])
    print("Produto:", produto["nome"])
    print("Quantidade:", produto["quantidade"])
    print(f"Preço: R$ {produto['preco']:.2f}")
    print("------------")


def mostrar_estoque():
    if not estoque:
        print("Estoque vazio.")
        return

    for produto in estoque:
        exibir_produto(produto)


def adicionar_produto():
    nome_produto = input("Nome do produto: ")

    if nome_produto.strip() == "":
        print("O nome do produto é inválido")
        return

    try:
        quantidade_produto = int(input("Quantidade do produto: "))
        if quantidade_produto <= 0:
            print("Valor inválido")
            return

        preco_produto = float(input("Valor do produto: "))
        if preco_produto <= 0:
            print("Valor inválido")
            return

    except ValueError:
        print("Por favor digite apenas números!")
        return

    produto = {
        "id": definir_id(),
        "nome": nome_produto,
        "quantidade": quantidade_produto,
        "preco": preco_produto,
    }

    estoque.append(produto)
    print("-------------------------------")
    print("Produto adicionado com sucesso!")
    print("-------------------------------")


def busca_id(lista, id_procurado):
    for item in lista:
        if item["id"] == id_procurado:
            return item
    return None


def pesquisar_produto():
    try:
        id_procurado = int(input("Digite o ID: "))
    except ValueError:
        print("Digite um número válido!")
        return

    resultado = busca_id(estoque, id_procurado)

    if resultado is None:
        print("Produto não encontrado.")
    else:
        exibir_produto(resultado)


def main():
    while True:
        print("""MENU DO ESTOQUE
    [1] - Adicionar produto
    [2] - Ver estoque
    [3] - Sair
    [4] - Pesquisar ID""")

        try:
            opcao = int(input("Digite a opção escolhida: "))
        except ValueError:
            print("Digite um número válido!")
            continue

        if opcao == 1:
            adicionar_produto()
        elif opcao == 2:
            mostrar_estoque()
        elif opcao == 3:
            print("Encerrando sistema...")
            break
        elif opcao == 4:
            pesquisar_produto()
        else:
            print("Opção inválida!")


if __name__ == "__main__":
    main()
