#Aluno Juan França Góes Dos Santos

#Função Para Cadastrar Os Produtos

class Carro:
    def __init__(self, codigo, nome, data_fabricacao, fornecedor , quantidade, valor_compra , cor):
        self.codigo = codigo
        self.nome = nome
        self.data_fabricacao = data_fabricacao
        self.fornecedor = fornecedor
        self.cor = cor
        self.quantidade = quantidade
        self.valor_compra = valor_compra

#Exibir Informações Sobre o Carro Escolhido

    def info_carro(self):
        return (
        f"Código: {self.codigo}\n"
        f"Nome: {self.nome}\n"
        f"Data de Fabricação: {self.data_fabricacao}\n"
        f"Fornecedor: {self.fornecedor}\n"
        f"Cor: {self.cor}\n"
        f"Quantidade: {self.quantidade}\n"
        f"Valor de Compra: R$ {self.valor_compra:.2f}"
    )


#Venda Dos Carros De Acordo Com Estoque

    def venda_carros(self, quantidade):
        if quantidade <= self.quantidade:
            self.quantidade -= quantidade
            return True
        return False

#Cadastro De Novo Veiculo

    def cadastro_veiculo():
        codigo = input ("Insira o Código do Carro: ")
        nome = input ("Insira o Nome do Carro: ")
        data = input ("Insira a Data de Fabricação (dd/mm/aaaa): ")
        fornecedor = input ("Insira o Nome do Fornecedor:  ")
        cor = input ("Insira a Cor do Veículo: ")
        quantidade = int (input("Insira a Quatidade Disponiveis: "))
        valor = float (input("Insira o Valor de Compra do Carro (R$): "))
        

#Função Para Cadastrar Estoque

class Estoque:
    def __init__(self):
        self.veiculos = []

#Adicionando Carro Ao Estoque

    def adicionar_carro(self, carro):
        for c in self.veiculos:
            if c.codigo == carro.codigo or c.nome.lower() == carro.nome.lower():
                print(" Esse Carro Já Possui no estoque.")
                return
        self.veiculos.append(carro)
        # print(" O Carro Foi Cadastrado Com Sucesso!")


#Exibir Estoque Com Todos Carros Disponiveis
    def mostrar_estoque(self):
        if not self.veiculos:
            print("Estoque vazio no momento!")
            return

        print("---------- ESTOQUE CARANGOS S/A ----------")
        for c in self.veiculos:
            print(c.info_carro())
            print("-" * 30)

#Função Para Realizar Venda

    def venda_veiculo(self):
        codigo = input("Digite o código do carro para venda: ")
        for c in self.veiculos:
            if c.codigo == codigo:
                try:
                    qtd = int(input("Quantidade a vender: "))
                    if c.venda_carros(qtd):
                        print(f" Venda realizada! Estoque restante: {c.quantidade}")
                    else:
                        print(" Quantidade indisponível no estoque.")
                    return
                except ValueError:
                    print("Essa Quantidade inválida.")
                    return
        print(" Carro não encontrado.")

#Função Para Procurar O Carro No Estoque
    
    def buscar_carro(self): 
        busca = input("Digite o nome ou código do carro: ").lower()
        for c in self.veiculos:
            if c.codigo.lower() == busca or c.nome.lower() == busca:
                print(" Carro Encontrado!:")
                print(c.info_carro())
                return
        print("Esse Carro Não Foi Encontrado No Estoque!")

#Calculando Custos Da Empresa

    def calcular_custos(self):
        total_semanal = sum(c.valor_compra * c.quantidade for c in self.veiculos)
        total_mensal = total_semanal * 4
        total_anual = total_mensal * 12
        print("\n--- CUSTOS ESTIMADOS ---")
        print(f"Custo semanal: R$ {total_semanal:.2f}")
        print(f"Custo mensal:  R$ {total_mensal:.2f}")
        print(f"Custo anual:   R$ {total_anual:.2f}")

      

#Função Principal Menu

def menu():
    estoque = Estoque()

    carros_iniciais = [
        Carro("001", "Gol", "01/01/2022", "Volkswagen", 3, 45000.0, "Prata"),
        Carro("002", "Onix", "15/03/2023", "Chevrolet", 5, 62000.0, "Branco"),
        Carro("003", "HB20", "10/04/2023", "Hyundai", 4, 58000.0, "Preto"),
        Carro("004", "Civic", "20/05/2021", "Honda", 2, 110000.0, "Cinza"),
        Carro("005", "Corolla", "11/02/2022", "Toyota", 3, 115000.0, "Preto"),
        Carro("006", "Fiesta", "30/06/2020", "Ford", 6, 39000.0, "Azul"),
        Carro("007", "Palio", "05/05/2019", "Fiat", 5, 30000.0, "Vermelho"),
        Carro("008", "Sandero", "17/09/2022", "Renault", 4, 47000.0, "Branco"),
        Carro("009", "Compass", "01/01/2023", "Jeep", 2, 150000.0, "Preto"),
        Carro("010", "Ka", "12/12/2021", "Ford", 3, 42000.0, "Prata")
    ]

    for carro in carros_iniciais:
        estoque.adicionar_carro(carro)

    while True:
        print("\n-------CARANGOS S/A-------")
        print("1. Cadastrar  Carro")
        print("2. Venda De Carro")
        print("3. Mostrar Estoque")
        print("4. Calcular Custos")
        print("5. Buscar Carro")
        print ("0. Para Sair")
        op = input("Escolha Uma Opção: ")

        if op == "1":
            codigo = input ("Insira o Código do Carro: ")
            nome = input ("Insira o Nome do Carro: ")
            data = input ("Insira a Data de Fabricação (dd/mm/aaaa): ")
            fornecedor = input ("Insira o Nome do Fornecedor:  ")
            cor = input ("Insira a Cor do Veículo: ")
            quantidade = int (input("Insira a Quatidade Disponiveis: "))
            valor = float (input("Insira o Valor de Compra do Carro (R$): "))
            carro = Carro(codigo, nome, data, fornecedor, quantidade, valor, cor)
            estoque.adicionar_carro(carro)
        elif op == "2":
            estoque.venda_veiculo()
        elif op == "3":
            estoque.mostrar_estoque()
        elif op == "4":
            estoque.calcular_custos()
        elif op == "5":
            estoque.buscar_carro()
        elif op == "0":
            print(" Sistema encerrado. Obrigado!")
            break
        else:
            print(" Opção inválida. Tente novamente.")

if __name__ == '__main__':
    menu()



