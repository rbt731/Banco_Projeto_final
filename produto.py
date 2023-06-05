import pymysql
class Produto:
    def conexao(self):
        con= pymysql.connect(
            host = "localhost",
            user = "root",
            password = "", 
            database = "loja_db"
        )

        return con
    
    def cadastrarProduto(self, codigo, nome, preco, quantidade):
        conexao = self.conexao()

        comando = "insert into produto values(%s, %s, %s, %s)"
        valores = (codigo, nome, preco, quantidade)
        consulta = conexao.cursor()

        consulta.execute(comando, valores)

        conexao.commit()

        print(consulta.rowcount, "linha inserida com sucesso\n")

        conexao.close()

    def consultarProdutos(self):
        conexao = self.conexao()

        comando = "select * from produto"
        consulta = conexao.cursor()
        consulta.execute(comando)

        resultado = consulta.fetchall()

        print("=-=-=-=-=-=-=-=-=-=-=-= TABELA DOS PRODUTOS =-=-=-=-=-=-=-=-=-=-=-=")
        
        con=0
        for i in resultado:
            con+=1
            print(f"Código: {i[0]}\t Nome: {i[1]}\t Preço: {i[2]}\t Quantidade: {i[3]}\n")
        print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n")
        print("=-=-=-=-= PRODUTOS CADASTRTADOS =-=-=-=-=\n") 
        print(f"Há {con} produtos cadastrados em sua tabela.\n")
        print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

        conexao.close()
    
    def deletarProdutos(self, codigo):
        conexao = self.conexao()

        comando = "delete from produto where cod_produto = %s"
        consulta = conexao.cursor()
        consulta.execute(comando, codigo)

        conexao.commit()

        if consulta.rowcount == 0:
            print("Erro: Nenhum item foi deletado")
        elif consulta.rowcount > 0:
            print(consulta.rowcount, "linhas deletadas com sucesso!")

        conexao.close()

    def atualizarNomeProdutos(self, nome, codigo):
        conexao = self.conexao()
        self.nome= nome
        self.codigo= codigo

        comando = "update produto set nome = %s where cod_produto = %s"
        valores = (self.nome, self.codigo)
        consulta = conexao.cursor()
        consulta.execute(comando, valores)

        conexao.commit()

        print(consulta.rowcount,"linha atualizada com sucesso\n")

        conexao.close()
    
    def atualizarPrecoProdutos(self, preco, codigo):
        conexao = self.conexao()
        self.preco= preco
        self.codigo= codigo

        comando = "update produto set preco = %s where cod_produto = %s"
        valores = (self.preco, self.codigo)
        consulta = conexao.cursor()
        consulta.execute(comando, valores)

        conexao.commit()

        print(consulta.rowcount,"linha atualizada com sucesso\n")

        conexao.close()

    def atualizarEstoqueProdutos(self, estoque, codigo):
        conexao = self.conexao()
        self.estoque = estoque
        self.codigo = codigo

        comando = "update produto set preco = %s where cod_produto = %s"
        valores = (self.estoque, self.codigo)
        consulta = conexao.cursor()
        consulta.execute(comando, valores)

        conexao.commit()

        print(consulta.rowcount,"linha atualizada com sucesso\n")

        conexao.close()
