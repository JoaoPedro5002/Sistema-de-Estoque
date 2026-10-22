# Sistema de Gerenciamento de Estoque (CLI)

Um sistema simples, robusto e interativo desenvolvido em **Python** para o gerenciamento de estoque direto pelo terminal (CLI). O projeto conta com tratamento de erros de entrada, validação de dados e identificação automática de produtos.

--|

## 🚀 Funcionalidades

- **[1] Adicionar Produto:** Cadastra novos itens informando nome, quantidade e preço, gerando um ID sequencial automático e validando entradas inválidas (valores negativos ou campos vazios).
- **[2] Ver Estoque:** Lista todos os produtos cadastrados atualmente no sistema de forma formatada.
- **[4] Pesquisar por ID:** Permite localizar rapidamente um produto específico informando o seu identificador único.
- **[3] Sair:** Encerra a execução do programa de forma segura.

--|

## 🛠️ Tecnologias Utilizadas

- Python 3.13.16 (Utiliza apenas bibliotecas nativas, sem dependências externas).

--|

## ⚙️ Como Executar o Projeto

1. Certifique-se de ter o **Python 3** instalado em sua máquina.
2. Baixe ou clone este repositório contendo o script Python.
3. Abra o terminal na pasta do projeto e execute o comando:

```bash
python Inventory System.py

MENU DO ESTOQUE
    [1] - Adicionar produto
    [2] - Ver estoque
    [3] - Sair
    [4] - Pesquisar ID

Basta digitar o número correspondente à operação desejada e seguir as instruções na tela. O sistema conta com validações para impedir que letras sejam digitadas onde números são esperados, além de evitar preços ou quantidades menores ou iguais a zero.
