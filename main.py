from produto import Produto
import os

p = Produto()
os.system("cls")
while True:
    escolha = int(input('''
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
Escolha qual função deseja realizar:
1 - Consultar produtos
2 - Cadastrar produtos
3 - Deletar Produtos
4 - Atualizar Produtos
5 - Sair
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

Digite a escolha: '''))
    #Escolha das consultas
    if escolha == 1:
        os.system("cls")
        p.consultarProdutos()
    
    #escolha de cadastro
    elif escolha == 2:
        os.system("cls")
        codigo = int(input("Informe o codigo do produto: "))
        nome  = input("Informe o nome do produto: ")
        preco = float(input("Informe o preço do produto: "))
        quant = int(input("Informe a quantidadde em estoque: "))
        os.system("cls")

        p.cadastrarProduto(codigo, nome, preco, quant)

    #Escolha de deletar produtos
    elif escolha == 3:
        os.system("cls")
        delete = int(input("Informe o código de produto que deseja deletar: "))
        p.deletarProdutos(delete)
    #Escolha de atualização
    elif escolha == 4:
        while True:
            escolha2 = int(input('''
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
Escolha qual função deseja realizar:
1 - Atualizar nome do produto
2 - Atualizar preço do produto
3 - Atualizar estoque do produto
4 - Sair
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
'''))
            #Atualização do nome
            if escolha2 == 1:
                os.system("cls")
                codigo = int(input("Informe o código do produto que deseja atualizar: "))
                nome = input("Informe o novo nome do produto: ")
                p.atualizarNomeProdutos(nome, codigo)

            #Atualização do preço
            elif escolha2 == 2:
                os.system("cls")
                codigo = int(input("Informe o código do produto que deseja atualizar: "))
                preco = float(input("Infome o novo preço do produto: "))
                p.atualizarPrecoProdutos(preco, codigo)

            #Atualização do estoque
            elif escolha2 == 3:
                os.system("cls")
                codigo = int(input("Informe o código do produto que deseja atualizar: "))
                estoque = int(input("Informe a nova quantidade do estoque do produto: "))
                p.atualizarEstoqueProdutos(estoque, codigo)

            #Sair da atualização
            elif escolha2 == 4:
                os.system("cls")
                break
    #Sair do Programa
    elif escolha == 5:
        os.system("cls")
        break
