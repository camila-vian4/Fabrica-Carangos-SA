import operacional
import financeiro

def voltarMenu():
    while True:
        print("\nDeseja continuar ou voltar ao menu principal? 🔄🏠")
        print("\n1. Continuar nesse módulo")
        print("2. Voltar ao menu principal")
        opcao_menu = input("\nSelecione a opção desejada: ").lower()

        if opcao_menu in ["1", "continuar", "c"]:
            return "continuar"  # aqui diz para quem chamou: continuar
        elif opcao_menu in ["2", "voltar", "v", "menu principal"]:
            return "voltar"  # aqui diz para quem chamou: voltar
        else:
            print("\nOpção inválida. Tente novamente. ❌")

producao_semana = None
agua = luz = salarios = impostos = None

print("\n\n")
print("--- Fábrica Carangos S/A 🚗✨")
print("Seja bem-vindo(a) ao nosso sistema! 🤖🛠️")

while True:

    print("\n\n🏠 > MENU PRINCIPAL:\n")
    print("1 - Módulo Operacional 📋")
    print("2 - Módulo de Estoque 📦")
    print("3 - Módulo Financeiro 💸")
    print("4 - Módulo de Recursos Humanos 👥")
    print("5 - Sair ❌")
    opcao = input("\n➡️  Escolha uma opção: ")

    # Inicializa as variáveis necessárias
    if opcao == "5":
        print("\nAgradecemos por utilizar nosso sistema! Até logo! 👋")
        exit()
    elif opcao not in ["1", "2", "3", "4"]:
        print("\nOpção inválida. Tente novamente. ❌")
        continue

    match opcao:

        case "1":
            while True:
            # Módulo Operacional
                print("\n\n--- MÓDULO OPERACIONAL | 📋✨")
                print("\n1. Cadastro de Produção 🚗")
                print("2. Simulação de Produção 📈")
                print("3. Projeção de Produção 📅")
                print("4. Relatório de Produção 📊")
                print("5. Sair ❌")
                opcao_operacional = input("\n➡️  Escolha uma opção: ")

                if opcao_operacional == "5":
                    print("\nAgradecemos por utilizar nosso sistema! Até logo! 👋")
                    exit()
                elif opcao_operacional not in ["1", "2", "3", "4", "5"]:
                    print("\nOpção inválida. Tente novamente. ❌")

                # Chamando as opções do módulo operacional
                match opcao_operacional:

                    case "1":
                        print("\n\n--- CADASTRO DE PRODUÇÃO | 🏭")
                        producao_semana = operacional.cadastrar_producao()
                        resposta = voltarMenu()
                        if resposta == "voltar":
                            break

                    case "2":
                        print("\n\n--- SIMULAÇÃO DE PRODUÇÃO | 📈")
                        if producao_semana is None:
                            print("\nNenhum cadastro encontrado! Cadastre antes de simular. ⚠️")
                        else:
                            total_geral, media_dia, media_turno, total_turno = operacional.calcular_totais(producao_semana)
                            producao_mensal, producao_anual = operacional.simular_projecoes(total_geral)
                            print(f"\nProdução mensal estimada: {producao_mensal} unidades")
                            print(f"Produção anual estimada: {producao_anual} unidades")
                        resposta = voltarMenu()
                        if resposta == "voltar":
                            break

                    case "3":
                        print("\n\n--- Projeção de Produção | 📅")
                        if producao_semana is None:
                            print("\nNenhum cadastro encontrado! Cadastre antes de emitir o relatório. ⚠️")
                        else:
                            capacidade_mensal_ideal, capacidade_anual_ideal = operacional.calcular_producao_ideal()
                            print(f"\nProdução mensal ideal: {capacidade_mensal_ideal} unidades")
                            print(f"Produção anual ideal: {capacidade_anual_ideal} unidades")
                        resposta = voltarMenu()
                        if resposta == "voltar":
                            break

                    case "4":
                        print("\n\n--- RELATÓRIO DE PRODUÇÃO | 📊\n")
                        if producao_semana is None:
                            print("\nNenhum cadastro encontrado! Cadastre antes de emitir o relatório. ⚠️")
                        else:
                            operacional.emitir_relatorio(producao_semana)
                        resposta = voltarMenu()
                        if resposta == "voltar":
                            break
        case "3":
            while True:
            # Módulo Financeiro
                print("\n\n--- MÓDULO FINANCEIRO | 💸✨")
                print("\n1. Despesas fixas 🧾")
                print("2. Custo por carro 🚗")
                print("3. Preço de venda (50% do lucro) 💰")
                print("4. Relatório financeiro 📊")
                print("5. Sair ❌")
                opcao_financeiro = input("\n➡️  Escolha uma opção: ")
                if opcao_financeiro == "5":
                    print("\nAgradecemos por utilizar nosso sistema! Até logo! 👋")
                    exit()
                elif opcao_financeiro not in ["1", "2", "3", "4", "5"]:
                    print("\nOpção inválida. Tente novamente. ❌")

                # Chamando as opções do módulo operacional
                match opcao_financeiro:

                    case "1":
                        print("\n\n--- DESPESAS FIXAS | 🧾\n")
                        agua, luz, salarios, impostos = financeiro.dados_financeiros()
                        custo_total = financeiro.calcular_custo_total(agua, luz, salarios, impostos)
                        print(f"\nCusto total das despesas fixas: R$ {custo_total:.2f}")
                        resposta = voltarMenu()
                        if resposta == "voltar":
                            break

                    case "2":
                        print("\n\n--- CUSTO POR CARRO | 🚗")
                        if producao_semana is None:
                            print("\nNenhum cadastro encontrado! Cadastre antes de calcular o custo por carro. ⚠️")
                        elif None in [agua, luz, salarios, impostos]:
                            print("\nVocê precisa cadastrar as despesas fixas antes! ❌")
                        else:
                            total_produzido = sum(turno for dia in producao_semana.values() for turno in dia.values())
                            custo_total = financeiro.calcular_custo_total(agua, luz, salarios, impostos)
                            custo_por_carro = financeiro.calcular_custo_por_carro(custo_total, total_produzido)
                            print(f"\nCusto por carro produzido: R$ {custo_por_carro:.2f}")
                        resposta = voltarMenu()
                        if resposta == "voltar":
                            break

                    case "3":
                        print("\n\n--- PREÇO DE VENDA | 💰\n")
                        if None in [agua, luz, salarios, impostos]:
                            print("\nCadastre as despesas fixas primeiro! ⚠️")
                        elif producao_semana is None:
                            print("\nCadastre a produção primeiro! ⚠️")
                        else:
                            total_produzido = sum(turno for dia in producao_semana.values() for turno in dia.values())
                            custo_total = financeiro.calcular_custo_total(agua, luz, salarios, impostos)
                            custo_por_carro = financeiro.calcular_custo_por_carro(custo_total, total_produzido)
                            preco_venda = financeiro.calcular_preco_venda(custo_por_carro)
                            print(f"\nPreço de venda sugerido (50% de lucro): R$ {preco_venda:.2f}")
                        resposta = voltarMenu()
                        if resposta == "voltar":
                            break

                    case "4":
                        print("\n\n--- RELATÓRIO FINANCEIRO | 📊\n")
                        if producao_semana is None:
                            print("\nNenhum cadastro encontrado! Cadastre antes de emitir o relatório financeiro. ⚠️")
                        elif None in [agua, luz, salarios, impostos]:
                            print("\nCadastre as despesas fixas primeiro! ⚠️")
                        else:
                            total_produzido = sum(turno for dia in producao_semana.values() for turno in dia.values())
                            financeiro.relatorio_financeiro(total_produzido, agua, luz, salarios, impostos)
                            resposta = voltarMenu()
                            if resposta == "voltar":
                                break