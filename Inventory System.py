estoque = []

def mostrar_estoque():
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
        print('O nome do produto é inválido')
        return
    
    def definir_id():
        if len(estoque) == 0:
            return 1
        else:
            ultimo_id = estoque[-1]
            return ultimo_id["id"] +1
    id_produto = definir_id()
    
    try:
        quantidade_produto = int(input("Quantidade do produto: "))
        if quantidade_produto <= 0:
            print('A quantidade inserida é inválida')
            return
        preco_produto = float(input("Valor do produto: "))
        if preco_produto <= 0: 
            print('O valor inserido é inválido')
            return
    except ValueError:
        print("Por favor digite apenas números!")
        return
    
    produto = {
    "id": id_produto,
    "nome": nome_produto,
    "quantidade": quantidade_produto, 
    "preco": preco_produto}
    
    estoque.append(produto)

def busca_id(lista, id_procurado):
    for item in lista:
        if item ["id"] == id_procurado:
            return item
    return None


while True:
    
    print("""MENU DO ESTOQUE
    [1] - Adicionar produto
    [2] - Ver estoque
    [3] - Sair 
    [4] - Pesquisar id """)
    
    opcao = int(input("Digite a opção escolhida: "))
    
    if opcao == 1:
        adicionar_produto()
    elif opcao == 2:
        mostrar_estoque()
    elif opcao == 3:
        break
    elif opcao == 4:
        id = int(input("Digite o id: "))
        resultado = busca_id(estoque, id)
        print(resultado)