estoque = []

def definir_id():
    if len(estoque) == 0:
        return 1
    else:
        ultimo_produto = estoque[-1]
        return ultimo_produto["id"] + 1


def mostrar_estoque():
    if len(estoque) == 0:
        print("Estoque vazio.")
        return

    for i in estoque:
        print("------------")
        print("ID:", i["id"])
        print("Produto:", i["nome"])
        print("Quantidade:", i["quantidade"])
        print("Preço:", i["preco"])
        print("------------")


def adicionar_produto():
    nome_produto = input("Nome do produto: ")

    if nome_produto.strip() == "":
        print("O nome do produto é inválido")
        return

    id_produto = definir_id()

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
        "id": id_produto,
        "nome": nome_produto,
        "quantidade": quantidade_produto,
        "preco": preco_produto
    }

    estoque.append(produto)
    print("Produto adicionado com sucesso!")


def busca_id(lista, id_procurado):
    for item in lista:
        if item["id"] == id_procurado:
            return item
    return None


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
        try:
            id_procurado = int(input("Digite o ID: "))
        except ValueError:
            print("Digite um número válido!")
            continue

        resultado = busca_id(estoque, id_procurado)

        if resultado is None:
            print("Produto não encontrado.")
        else:
            print("------------")
            print("ID:", resultado["id"])
            print("Produto:", resultado["nome"])
            print("Quantidade:", resultado["quantidade"])
            print("Preço:", resultado["preco"])
            print("------------")

    else:
        print("Opção inválida!")
