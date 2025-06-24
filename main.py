import operacional    
import estoque as estoque_modulo  
import financeiro      
import recursos_humanos     

def voltarMenu(): # Função para voltar ao menu principal ou continuar no módulo atual
    while True:
        print("\nDeseja continuar ou voltar ao menu principal? 🔄🏠")
        print("\n1. Continuar nesse módulo")
        print("2. Voltar ao menu principal")
        opcao_menu = input("\nSelecione a opção desejada: ").lower()

        if opcao_menu in ["1", "continuar", "c"]:
            return "continuar"  # Retorna para continuar no módulo atual
        elif opcao_menu in ["2", "voltar", "v", "menu principal"]:
            return "voltar"     # Retorna para o menu principal
        else:
            print("\nOpção inválida. Tente novamente. ❌")

producao_semana = None # Variável para armazenar a produção da semana
agua = luz = salarios = impostos = None # Variáveis para armazenar as despesas fixas
estoque = estoque_modulo.Estoque() # Instancia o módulo de estoque

print("\n\n")
print("--- Fábrica Carangos S/A 🚗✨")
print("Seja bem-vindo(a) ao nosso sistema! 🤖🛠️")

while True: # Loop principal do sistema

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
        exit() # Encerra o programa
    elif opcao not in ["1", "2", "3", "4"]:
        print("\nOpção inválida. Tente novamente. ❌")
        continue # Volta ao início do loop principal

    match opcao: # Estrutura de seleção para os módulos principais

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

                if opcao_operacional == "5": # Opção para sair do módulo operacional
                    print("\nAgradecemos por utilizar nosso sistema! Até logo! 👋")
                    exit()
                elif opcao_operacional not in ["1", "2", "3", "4", "5"]: # Verifica se a opção é válida
                    print("\nOpção inválida. Tente novamente. ❌")

                # Chamando as opções do módulo operacional
                match opcao_operacional:

                    case "1":
                        print("\n\n--- CADASTRO DE PRODUÇÃO | 🏭") 
                        producao_semana = operacional.cadastrar_producao() # Chama a função para cadastrar a produção
                        resposta = voltarMenu() # Pergunta se deseja voltar ao menu principal ou continuar
                        if resposta == "voltar": # Se a resposta for voltar, sai do loop
                            break

                    case "2":
                        print("\n\n--- SIMULAÇÃO DE PRODUÇÃO | 📈")
                        if producao_semana is None: # Verifica se a produção foi cadastrada
                            print("\nNenhum cadastro encontrado! Cadastre antes de simular. ⚠️")
                        else:
                            # Calcula totais e simula projeções mensais e anuais
                            total_geral, media_dia, media_turno, total_turno = operacional.calcular_totais(producao_semana)
                            producao_mensal, producao_anual = operacional.simular_projecoes(total_geral)
                            print(f"\nProdução mensal estimada: {producao_mensal} unidades")
                            print(f"Produção anual estimada: {producao_anual} unidades")
                        resposta = voltarMenu()
                        if resposta == "voltar":
                            break

                    case "3":
                        print("\n\n--- PROJEÇÃO DE SIMULAÇÃO | 📅")
                        if producao_semana is None: # Verifica se a produção foi cadastrada
                            print("\nNenhum cadastro encontrado! Cadastre antes de emitir o relatório. ⚠️") 
                        else:
                            # Calcula capacidade ideal mensal e anual
                            capacidade_mensal_ideal, capacidade_anual_ideal = operacional.calcular_producao_ideal() # Chama a função para calcular a capacidade ideal
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
                            operacional.emitir_relatorio(producao_semana) # Emite o relatório de produção
                        resposta = voltarMenu()
                        if resposta == "voltar":
                            break

        case "2":
            while True:
                # Módulo de Estoque
                print("\n\n--- MÓDULO DE ESTOQUE | 📦✨")
                print("\n1. Cadastrar Carro 🚗")
                print("2. Vender Carro 🏷️")
                print("3. Mostrar Estoque 📋")
                print("4. Calcular Custos 💰")
                print("5. Buscar Carro 🔍")
                print("6. Sair ❌")
                opcao_estoque = input("\n➡️  Escolha uma opção: ")
                if opcao_estoque == "6":
                    print("\nAgradecemos por utilizar nosso sistema! Até logo! 👋")
                    exit()
                elif opcao_estoque not in ["1", "2", "3", "4", "5", "6"]:
                    print("\nOpção inválida. Tente novamente. ❌")

                # Chamando as opções do módulo de estoque
                match opcao_estoque:
                    case "1":
                        print("\n\n--- CADASTRO DE CARRO | 🚗\n")
                        # Coleta dados do carro a ser cadastrado
                        codigo = input("Código: ")
                        nome = input("Nome: ")
                        data_fabricacao = input("Data de fabricação: ")
                        fornecedor = input("Fornecedor: ")
                        cor = input("Cor: ")

                        try: # Try para capturar erros de entrada
                            quantidade = int(input("Quantidade: "))
                            valor_compra = float(input("Valor de compra: "))
                        except ValueError: # except para tratar entradas inválidas
                            print("Valores inválidos! ❌")
                            break

                        # Cria novo carro e adiciona ao estoque
                        novo_carro = estoque_modulo.Carro(codigo, nome, data_fabricacao, fornecedor, quantidade, valor_compra, cor) # Instancia um novo carro
                        estoque.adicionar_carro(novo_carro) # Adiciona o carro ao estoque
                        resposta = voltarMenu()
                        if resposta == "voltar":
                            break

                    case "2":
                        print("\n\n--- VENDA DE CARRO | 🏷️\n")
                        estoque.venda_veiculo() # Realiza a venda de um veículo
                        resposta = voltarMenu() # Pergunta se deseja voltar ao menu principal ou continuar
                        if resposta == "voltar":
                            break

                    case "3":
                        print("\n\n--- MOSTRAR ESTOQUE | 📋\n")
                        estoque.mostrar_estoque() # Mostra todos os carros em estoque
                        resposta = voltarMenu() # Pergunta se deseja voltar ao menu principal ou continuar
                        if resposta == "voltar":
                            break

                    case "4":
                        print("\n\n--- CÁLCULO DE CUSTOS | 💰")
                        estoque.calcular_custos() # Calcula custos do estoque
                        resposta = voltarMenu() # Pergunta se deseja voltar ao menu principal ou continuar
                        if resposta == "voltar":
                            break

                    case "5":
                        print("\n\n--- BUSCAR CARRO | 🔍\n")
                        estoque.buscar_carro() # Busca um carro pelo código ou nome
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

                # Chamando as opções do módulo financeiro
                match opcao_financeiro:

                    case "1":
                        print("\n\n--- DESPESAS FIXAS | 🧾\n")
                        # Coleta dados das despesas fixas
                        agua, luz, salarios, impostos = financeiro.dados_financeiros() # Chama a função para coletar os dados financeiros
                        custo_total = financeiro.calcular_custo_total(agua, luz, salarios, impostos) # Calcula o custo total
                        print(f"\nCusto total das despesas fixas: R$ {custo_total:.2f}") # Exibe o custo total
                        resposta = voltarMenu()
                        if resposta == "voltar":
                            break

                    case "2":
                        print("\n\n--- CUSTO POR CARRO | 🚗")
                        if producao_semana is None: # Verifica se a produção foi cadastrada
                            print("\nNenhum cadastro encontrado! Cadastre antes de calcular o custo por carro. ⚠️") # Exibe mensagem de erro
                        elif None in [agua, luz, salarios, impostos]: # Verifica se as despesas fixas foram cadastradas
                            print("\nVocê precisa cadastrar as despesas fixas antes! ❌")
                        else:
                            total_produzido = sum(turno for dia in producao_semana.values() for turno in dia.values()) # Calcula o total produzido na semana
                            custo_total = financeiro.calcular_custo_total(agua, luz, salarios, impostos) # Calcula o custo total
                            custo_por_carro = financeiro.calcular_custo_por_carro(custo_total, total_produzido) # Calcula o custo por carro
                            print(f"\nCusto por carro produzido: R$ {custo_por_carro:.2f}")
                        resposta = voltarMenu()
                        if resposta == "voltar":
                            break

                    case "3":
                        print("\n\n--- PREÇO DE VENDA | 💰\n")
                        if None in [agua, luz, salarios, impostos]: # Verifica se as despesas fixas foram cadastradas
                            print("\nCadastre as despesas fixas primeiro! ⚠️")
                        elif producao_semana is None: # Verifica se a produção foi cadastrada
                            print("\nCadastre a produção primeiro! ⚠️")
                        else:
                            total_produzido = sum(turno for dia in producao_semana.values() for turno in dia.values()) # Calcula o total produzido na semana
                            custo_total = financeiro.calcular_custo_total(agua, luz, salarios, impostos) # Calcula o custo total
                            custo_por_carro = financeiro.calcular_custo_por_carro(custo_total, total_produzido) # Calcula o custo por carro
                            preco_venda = financeiro.calcular_preco_venda(custo_por_carro) # Calcula o preço de venda com 50% de lucro
                            print(f"\nPreço de venda sugerido (50% de lucro): R$ {preco_venda:.2f}")
                        resposta = voltarMenu()
                        if resposta == "voltar":
                            break

                    case "4":
                        print("\n\n--- RELATÓRIO FINANCEIRO | 📊\n")
                        if producao_semana is None:
                            print("\nNenhum cadastro encontrado! Cadastre antes de emitir o relatório financeiro. ⚠️")
                        elif None in [agua, luz, salarios, impostos]: # Verifica se as despesas fixas foram cadastradas
                            print("\nCadastre as despesas fixas primeiro! ⚠️")
                        else:
                            total_produzido = sum(turno for dia in producao_semana.values() for turno in dia.values()) # Calcula o total produzido na semana
                            financeiro.relatorio_financeiro(total_produzido, agua, luz, salarios, impostos) # Gera o relatório financeiro
                            resposta = voltarMenu()
                            if resposta == "voltar":
                                break
        case "4":
            while True:
                # Módulo Recursos Humanos
                print("\n\n--- MÓDULO RECURSOS HUMANOS | 👥✨")
                print("\n1. Cadastrar Funcionário 📝")
                print("2. Calcular Salário 💰")
                print("3. Gerar Relatório Final 📊")
                print("4. Sair ❌")
                opcao_rh = input("\n➡️  Escolha uma opção: ")
                if opcao_rh == "4":
                    print("\nAgradecemos por utilizar nosso sistema! Até logo! 👋")
                    exit()
                elif opcao_rh not in ["1", "2", "3", "4"]: # Verifica se a opção é válida
                    print("\nOpção inválida. Tente novamente. ❌")

                # Chamando as opções do módulo de recursos humanos
                match opcao_rh:
                    case "1":
                        print("\n\n--- CADASTRO DE FUNCIONÁRIO | 📝\n")
                        recursos_humanos.cadastrar_funcionario() # Chama a função para cadastrar um novo funcionário
                        resposta = voltarMenu()
                        if resposta == "voltar":
                            break

                    case "2":
                        print("\n\n--- CÁLCULO DE SALÁRIO | 💰\n")
                        recursos_humanos.calcular_salario() # Chama a função para calcular o salário de um funcionário
                        resposta = voltarMenu()
                        if resposta == "voltar":
                            break

                    case "3":
                        print("\n\n--- RELATÓRIO FINAL | 📊\n")
                        recursos_humanos.gerar_relatorio() # Gera o relatório final com todos os funcionários cadastrados
                        resposta = voltarMenu()
                        if resposta == "voltar":
                            break
                      