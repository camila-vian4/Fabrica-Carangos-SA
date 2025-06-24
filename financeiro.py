# Aluna: Camila Viana Lopes
# Módulo 3 - Financeiro

def solicitar_numero(mensagem, tipo="float"):
    while True:
        entrada = input(mensagem).replace(',', '.')
        try:
            if tipo == "int":
                return int(entrada)
            else:
                return float(entrada)
        except ValueError:
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

def dados_financeiros():
    agua = solicitar_numero("💧 > Informe o valor da conta de água: R$ ")
    luz = solicitar_numero("💡 > Informe o valor da conta de luz: R$ ")
    salarios = solicitar_numero("💲 > Informe o valor total dos salários: R$ ")
    impostos = solicitar_numero("💵 > Informe o valor dos impostos: R$ ")
    return agua, luz, salarios, impostos

def calcular_custo_total(agua, luz, salarios, impostos):
    return agua + luz + salarios + impostos

def calcular_custo_por_carro(custo_total, total_produzido):
    if total_produzido == 0:
        return 0  # Evita divisão por zero
    return custo_total / total_produzido

def calcular_preco_venda(custo_por_carro):
    return custo_por_carro * 1.5  # 50% de lucro

def relatorio_financeiro(total_produzido, agua, luz, salarios, impostos):
    custo_total = calcular_custo_total(agua, luz, salarios, impostos)
    custo_por_carro = calcular_custo_por_carro(custo_total, total_produzido)
    preco_venda = calcular_preco_venda(custo_por_carro)

    dicio_relatorio_financeiro = {
        "💧 Água": agua,
        "💡 Luz": luz,
        "💲 Salários": salarios,
        "💵 Impostos": impostos,
        "🟢 Custo Total de Produção": custo_total,
        "🔴 Custo por Carro": custo_por_carro,
        "🟡 Preço de Venda (50% de lucro)": preco_venda
    }

    for chave, valor in dicio_relatorio_financeiro.items():
        print(f"{chave}: R$ {valor:.2f}")