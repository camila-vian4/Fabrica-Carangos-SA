# Aluna: Camila Viana Lopes
# Módulo 3 - Financeiro

def calcular_custo_total(agua, luz, salarios, impostos):
    return agua + luz + salarios + impostos

def calcular_custo_por_carro(custo_total, total_produzido):
    if total_produzido == 0:
        return 0  # Evita divisão por zero
    return custo_total / total_produzido

def calcular_preco_venda(custo_por_carro):
    return custo_por_carro * 1.5  # Adiciona 50% de lucro

def financeiro():
    # Cabeçalho do módulo
    print("\n----- MÓDULO FINANCEIRO | Fábrica Carangos S/A > 💵✨ -----\n")
    
    # Entradas
    agua = float(input("💧 > Informe o valor da conta de água: R$ "))
    luz = float(input("💡 > Informe o valor da conta de luz: R$ "))
    salarios = float(input("💲 > Informe o valor total dos salários: R$ "))
    impostos = float(input("💵 > Informe o valor dos impostos: R$ "))
    
    # IMPORTANTE: O valor abaixo precisa ser integrado com o Módulo Operacional
    total_produzido = int(input("🚗 > Informe o total de carros produzidos na semana: "))
    
    # Cálculos
    custo_total = calcular_custo_total(agua, luz, salarios, impostos)
    custo_por_carro = calcular_custo_por_carro(custo_total, total_produzido)
    preco_venda = calcular_preco_venda(custo_por_carro)
    
    # Saídas
    print(f"\n🟢 > Custo total de produção: R$ {custo_total:.2f}")
    print(f"🔴 > Custo por carro: R$ {custo_por_carro:.2f}")
    print(f"🟡 > Preço de venda (50% de lucro): R$ {preco_venda:.2f}")

# financeiro()