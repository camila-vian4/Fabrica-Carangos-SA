# módulo rh.py - Marcos Vinicius

# Lista onde ficam todos os funcionários cadastrados
funcionarios = []


# Função pra cadastrar um novo funcionário com todos os dados necessários
def cadastrar_funcionario():
    
    # Coleta as infos básicas deixando tudo minusculo e ignorando espacos
    nome = input("nome: ").strip().lower()
    cpf = input("cpf: ").strip()
    rg = input("rg: ").strip()
    endereco = input("endereço: ").strip().lower()
    telefone = input("telefone: ").strip()

    # Confirma se o cargo é válido (só aceita 3 tipos)
    while True:
        cargo = input("cargo (operador / gerente / diretor): ").strip().lower()
        if cargo not in ['operador', 'gerente', 'diretor']:
            print("cargo inválido.")
        else:
            break

    # Pergunta se tem filhos, e quantos são e já inclui o input do usuario num verificador padrão de erros.
    while True:
        tem_filho = input("possui filhos? (s/n): ").strip().lower()
        if tem_filho in ['s', 'sim']:
            try:
                qntd_filhos = int(input("qtde filhos: "))
                break
            except ValueError:
                print("entrada inválida.")
        elif tem_filho in ['n', 'nao', 'não']:
            qntd_filhos = 0
            break
        else:
            print("responda com s ou n.")

    # Cria o funcionário como um dicionário
    funcionario = {
        'nome': nome,
        'cpf': cpf,
        'rg': rg,
        'endereco': endereco,
        'telefone': telefone,
        'cargo': cargo,
        'filhos': qntd_filhos,
        'salario_bruto': 0,     # já deixa pronto pro cálculo
        'ir': 0,
        'salario_liquido': 0
    }

    # Salva o funcionário na lista, onde como ja foi dito, cada funcionario é um dicionario
    funcionarios.append(funcionario)
    print(f"\n{nome.title()} cadastrado com sucesso.\n")


# Função pra calcular o salário do funcionário pelo CPF
def calcular_salario():
    cpf_digitado = input("cpf do funcionário: ").strip()
    funcionario = None

    # Procura na lista o funcionário com o CPF informado
    for f in funcionarios:
        if f['cpf'] == cpf_digitado:
            funcionario = f
            break

#caso nao tenha funcionario
    if not funcionario:
        print("funcionário não encontrado.")
        return

    # Define o valor da hora com base no cargo
    cargo = funcionario['cargo']
    if cargo == 'operador':
        salario_hora = 10.00
    elif cargo == 'gerente':
        salario_hora = 22.73
    elif cargo == 'diretor':
        salario_hora = 36.36
    else:
        print("cargo inválido.")
        return

    # Pede a quantidade de horas que ele trabalhou no mês
    while True:
        try:
            horas_trabalhadas = int(input("horas trabalhadas no mês: "))
            break
        except ValueError:
            print("entrada inválida.")

    # Calcula horas normais (até 220h) e horas extras (só operador tem extra)
    horas_normais = min(horas_trabalhadas, 220)
    horas_extras = max(horas_trabalhadas - 220, 0)

    if cargo == 'operador':
        valor_horas_extras = horas_extras * salario_hora * 1.5  # operador ganha 50% a mais na extra
    else:
        valor_horas_extras = 0  # gerente e diretor não ganham hora extra

    # Soma tudo pra formar o salário bruto
    salario_bruto = (horas_normais * salario_hora) + valor_horas_extras

    # Aplica o desconto do IR baseado na faixa salarial
    if salario_bruto <= 2112:
        ir = 0
    elif salario_bruto <= 2826.65:
        ir = (salario_bruto * 0.075) - 158.40
    elif salario_bruto <= 3751.05:
        ir = (salario_bruto * 0.15) - 370.40
    elif salario_bruto <= 4664.68:
        ir = (salario_bruto * 0.225) - 651.73
    else:
        ir = (salario_bruto * 0.275) - 884.96

    # Resultado final: salário líquido
    salario_liquido = salario_bruto - ir

    # Atualiza os dados salariais no cadastro do funcionário
    funcionario['salario_bruto'] = salario_bruto
    funcionario['ir'] = ir
    funcionario['salario_liquido'] = salario_liquido

    # Mostra tudo na tela
    print("\n--- cálculo de salário ---")
    print(f"nome: {funcionario['nome'].title()}")
    print(f"cargo: {cargo}")
    print(f"salário bruto: R$ {salario_bruto:.2f}")
    print(f"IRPF: R$ {ir:.2f}")
    print(f"salário líquido: R$ {salario_liquido:.2f}\n")


# Relatório final com todos os dados + salário de cada funcionário
def gerar_relatorio():
    print("\n========= RELATÓRIO FINAL =========")
    
    if not funcionarios:
        print("nenhum funcionário cadastrado.")
        return

    # Passa por cada funcionário e mostra tudo, com base no indice(f), que nesse caso, é cada funcionario da lista
    for f in funcionarios:
        print(f"\nfuncionário: {f['nome'].title()}")
        print(f"cpf: {f['cpf']}")
        print(f"cargo: {f['cargo']}")
        print(f"telefone: {f['telefone']}")
        print(f"endereço: {f['endereco']}")
        print(f"filhos: {f['filhos']}")
        print(f"salário bruto: R$ {f['salario_bruto']:.2f}")
        print(f"IRPF: R$ {f['ir']:.2f}")
        print(f"salário líquido: R$ {f['salario_liquido']:.2f}")
    
    print("\n========= FIM DO RELATÓRIO =========\n")


# Menu principal: aqui o usuário escolhe o que quer fazer
def menu():
    
    # como foi pedido, fazemos o cadastro de 5 funcionarios no minimo
    while len(funcionarios) < 5:
        print(f"\nCadastro de funcionarios")
        cadastrar_funcionario()

    # Depois dos 5, libera o menu geral
    while True:
        print("\n=== MENU RH ===")
        print("[1] Cadastrar novo funcionário")
        print("[2] Calcular salário")
        print("[3] Gerar relatório final")
        print("[0] Sair")

        opcao = input("opção: ").strip()

        if opcao == "1":
            cadastrar_funcionario()
        elif opcao == "2":
            calcular_salario()
        elif opcao == "3":
            gerar_relatorio()
        elif opcao == "0":
            print("encerrando o sistema.")
            break
        else:
            print("opção inválida.")


# Chama o menu quando o arquivo for executado
menu()
