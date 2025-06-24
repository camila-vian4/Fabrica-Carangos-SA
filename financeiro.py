# Aluna: Camila Viana Lopes
# Módulo 3 - Financeiro

def solicitar_numero(mensagem, tipo="float"): # Função para solicitar um número ao usuário
    while True:
        entrada = input(mensagem).replace(',', '.') # Substitui vírgula por ponto para aceitar números decimais
        try:
            if tipo == "int": # Verifica se o tipo é inteiro
                return int(entrada) # Converte a entrada para inteiro
            else:
                return float(entrada) # Converte a entrada para float
        except ValueError: # ValueError é lançado se a conversão falhar
            print("\nErro! Valor inválido. ❌")
            print("\nDeseja tentar novamente?")
            print("\n1. Sim")
            print("2. Não")
            opcao = input("\nSelecione a opção desejada: ").lower()
            if opcao not in ["1", "s", "sim", "ss"]:
                print("\nSaindo do módulo financeiro... 💰👋")
                exit()
            else:
                print("Tentando novamente... 🔄\n")

def dados_financeiros(): # Função para coletar dados financeiros
    agua = solicitar_numero("💧 > Informe o valor da conta de água: R$ ")
    luz = solicitar_numero("💡 > Informe o valor da conta de luz: R$ ")
    salarios = solicitar_numero("💲 > Informe o valor total dos salários: R$ ")
    impostos = solicitar_numero("💵 > Informe o valor dos impostos: R$ ")
    return agua, luz, salarios, impostos

def calcular_custo_total(agua, luz, salarios, impostos): # Função para calcular o custo total de produção
    return agua + luz + salarios + impostos

def calcular_custo_por_carro(custo_total, total_produzido): # Função para calcular o custo por carro produzido
    if total_produzido == 0: #
        return 0  # Evita divisão por zero
    return custo_total / total_produzido

def calcular_preco_venda(custo_por_carro): # Função para calcular o preço de venda com 50% de lucro
    return custo_por_carro * 1.5  # 50% de lucro

def relatorio_financeiro(total_produzido, agua, luz, salarios, impostos): # Função para gerar o relatório financeiro
    custo_total = calcular_custo_total(agua, luz, salarios, impostos) # Calcula o custo total
    custo_por_carro = calcular_custo_por_carro(custo_total, total_produzido) # Calcula o custo por carro
    preco_venda = calcular_preco_venda(custo_por_carro) # Calcula o preço de venda

    dicio_relatorio_financeiro = {   # # Dicionário para armazenar os dados do relatório financeiro
        "💧 Água": agua,
        "💡 Luz": luz,
        "💲 Salários": salarios,
        "💵 Impostos": impostos,
        "🟢 Custo Total de Produção": custo_total,
        "🔴 Custo por Carro": custo_por_carro,
        "🟡 Preço de Venda (50% de lucro)": preco_venda
    }

    for chave, valor in dicio_relatorio_financeiro.items(): # Itera sobre o dicionário e imprime os valores formatados
        print(f"{chave}: R$ {valor:.2f}") # Imprime cada chave e valor com duas casas decimais
        #chave é o emoji e o valor é o custo ou preço calculado