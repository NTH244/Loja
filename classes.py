import os

class Loja:
    def __init__(self, nome, endereco, cnpj):
        self.nome = nome
        self.endereco = endereco
        self.cnpj = cnpj

class Cliente:
    def __init__(self):
        self.clientes = []
        self.carrinho = []

    def adicionar_cliente(self, nome, senha):
        self.clientes.append({"nome": nome, "senha": senha})

    def listar_clientes(self):
        for i, cliente in enumerate(self.clientes):
            print(f"Índice: {i}  |  Nome: {cliente['nome']}  |  Senha: {cliente['senha']}")

    def logar_cliente(self, nome, senha):
        return any(cliente['nome'] == nome and cliente['senha'] == senha for cliente in self.clientes)

    def remover_cliente(self, indice):
        if indice < len(self.clientes):
            del self.clientes[indice]
            print("Cliente removido com sucesso")
        else:
            print("Não existe esse cliente")

class Produto:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor

class Produtos:
    def __init__(self):
        self.lista_loja = []
        self.lista_carrinho = []
        self.compras_realizadas = []

    def inserir_produto_loja(self, produto):
        self.lista_loja.append(produto)
        print(f"Produto '{produto.nome}' foi adicionado à lista da loja.")

    def listar_produtos_loja(self):
        for i, produto in enumerate(self.lista_loja, start=1):
            print(f"{i} -> Nome: {produto.nome}, Valor: {produto.valor}")

    def get_produto_loja(self, indice):
        if 0 <= indice < len(self.lista_loja):
            return self.lista_loja[indice]
        else:
            return None

    def del_produto_loja(self, indice):
        if 0 <= indice < len(self.lista_loja):
            del self.lista_loja[indice]
            print("Produto removido da lista da loja.")
        else:
            print("Produto não encontrado na lista da loja.")

    def add_produto_carrinho(self, indice):
        produto = self.get_produto_loja(indice)
        if produto:
            self.lista_carrinho.append(produto)
            print("Produto adicionado ao carrinho.")
        else:
            print("Produto não encontrado na lista da loja.")

    def listar_produtos_carrinho(self):
        for i, produto in enumerate(self.lista_carrinho, start=1):
            print(f"{i} -> Nome: {produto.nome}, Valor: {produto.valor}")

    def del_produto_carrinho(self, indice):
        if 0 <= indice < len(self.lista_carrinho):
            del self.lista_carrinho[indice]
            print("Produto removido do carrinho.")
        else:
            print("Produto não encontrado no carrinho.")

    def realizar_compra(self, cliente):
        if not self.lista_carrinho:
            print("Carrinho vazio. Adicione produtos ao carrinho antes de realizar a compra.")
            return

        total = sum(produto.valor for produto in self.lista_carrinho)
        compra = {
            "produtos": [produto.nome for produto in self.lista_carrinho],
            "valor_total": total
        }
        self.compras_realizadas.append(compra)

        print("Produtos no carrinho:")
        for i, produto in enumerate(self.lista_carrinho, start=1):
            print(f"{i} -> Nome: {produto.nome}, Valor: {produto.valor}")
        print(f"Total da compra: {total}")

        opcao = input("Deseja confirmar a compra? (S/N): ")
        if opcao.lower() == "s":
            print("Compra realizada com sucesso!")
            self.lista_carrinho.clear()
        else:
            print("Compra cancelada.")

    def gerar_relatorio_vendas(self):
        if not self.compras_realizadas:
            print("Não há vendas registradas.")
            return

        print("\n=== Relatório de Todas as Vendas ===")
        for i, compra in enumerate(self.compras_realizadas, start=1):
            print(f"Venda {i}:")
            print(f"Produtos: {', '.join(compra['produtos'])}")
            print(f"Valor Total: {compra['valor_total']}\n")

    def gerar_relatorio_compras(self):
        print("\n=== Relatório de Compras ===")
        for i, compra in enumerate(self.compras_realizadas, start=1):
            print(f"Compra {i}:")
            print(f"Produtos: {', '.join(compra['produtos'])}")
            print(f"Valor Total: {compra['valor_total']}\n")

class Adm:
    def __init__(self):
        self.adms = [{"nome": "admin", "senha": "admin"}]

    def cadastrar_adm(self, nome, senha):
        novo_adm = {"nome": nome, "senha": senha}
        self.adms.append(novo_adm)

    def verificar_adm(self, nome, senha):
        for adm in self.adms:
            if adm["nome"] == nome and adm["senha"] == senha:
                return True
        return False

    def listar_adms(self):
        for i, adm in enumerate(self.adms):
            print(f" Índice: {i}  |  Nome: {adm['nome']}  |  Senha: {adm['senha']}")

    def remover_adm(self, indice):
        if indice == 0:
            print("Não é possível remover o administrador padrão.")
        elif 0 < indice < len(self.adms):
            del self.adms[indice]
        else:
            print("Não existe esse administrador.")
