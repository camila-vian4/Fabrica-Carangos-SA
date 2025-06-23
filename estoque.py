#Aluno Juan França Góes Dos Santos

#Dicionário Com Os Dados Do Carro

carro = {
    'codigo': codigo,
    'nome': nome,
    'data_fabricacao': data_fabricacao,
    'fornecedor': fornecedor,
    'cor': cor,
    'quantidade': quantidade,
    'valor_compra': valor_compra
}


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
        return f"{self.nome} {self.data_fabricacao} {self.fornecedor} {self.cor} {self.quantidade} {self.valor_compra}"

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

    def adicionando_carros(self, veiculos):
        for c in self.veiculos:
            if c.codigo == carro.codigo or c.nome.lower() == carro.nome.lower():
                print(" Esse Carro Já Possui no estoque.")
                return
        self.veiculos.append(carro)
        print(" O Carro Foi Cadastrado Com Sucesso!")


#Exibir Estoque Com Todos Carros Disponiveis
    def mostrar_estoque(self):
        for Carro in self.veiculos:
            if not self.veiculos:
                print("Estoque Vazio No Momento, Verifique Disponibilidade Outro Dia!")
        else:
            print("----------ESTOQUE CARANGOS S/A--------------")
            print(carro.info_carro())

#Função Para Realizar Venda

    def venda_veiculo():
        venda_codigo = input("Código do Carro Para Realizar a Venda: ")
        

#Função Principal Menu

def menu():

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
        elif op == "0":
            ("Sistema Encerrando...!")
            break

        else:
            print("Opção Inválida, Por favor Tente Novamente!")


