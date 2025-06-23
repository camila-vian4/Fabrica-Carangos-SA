import operacional
from financeiro import financeiro

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
                print("2. Relatório de Produção 📊")
                print("3. Simulação de Produção 📈")
                print("4. Projeção de Produção 📅")
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
                        print("\n\n--- RELATÓRIO DE PRODUÇÃO | 📊\n")
                        if producao_semana is None:
                            print("\nNenhum cadastro encontrado! Cadastre antes de emitir o relatório. ⚠️")
                        else:
                            operacional.emitir_relatorio(producao_semana)
                        resposta = voltarMenu()
                        if resposta == "voltar":
                            break
                    case "3":
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
        

# producao_semana = operacional.cadastrar_producao()
# total_geral, media_dia, media_turno, total_turno = operacional.calcular_totais(producao_semana)
# producao_mensal, producao_anual = operacional.simular_projecoes(total_geral)
# capacidade_mensal_ideal, capacidade_anual_ideal = operacional.calcular_producao_ideal()
# operacional.emitir_relatorio(producao_semana)
# abastecimento.voltarMenu()