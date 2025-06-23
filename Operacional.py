# Aluno Rodrigo Costa dos santos


# Função para cadastrar a produção de cada turno (manhã, tarde, noite) por 7 dias da semana
def cadastrar_producao():
    print("\nCadastro da produção diária (manhã, tarde, noite):\n")
    dias = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]  # Dias da semana
    turnos = ["manha", "tarde", "noite"]  # Turnos do dia
    producao_semana = {}  # Dicionário para armazenar os dados

    # Loop para cada dia da semana
    for dia in dias:
        producao_semana[dia] = {}  # Inicializa o dicionário do dia
        # Loop para cada turno
        for turno in turnos:
            while True:
                try:
                    # Solicita ao usuário o valor da produção e armazena
                    valor = int(input(f"Informe a produção para {dia} - {turno}: "))
                    producao_semana[dia][turno] = valor
                    break  # Sai do loop se o valor for válido
                except ValueError:
                    print("Digite um número válido!")  # Mensagem em caso de erro
    return producao_semana  # Retorna os dados cadastrados

# Função para calcular totais e médias
def calcular_totais(producao_semana):
    total_geral = 0  # Soma da produção total na semana
    total_turno = {"manha": 0, "tarde": 0, "noite": 0}  # Soma por turno
    dias_contados = 0  # Contador de dias

    # Loop por dia da semana
    for dia in producao_semana:
        turnos = producao_semana[dia]
        total_dia = turnos["manha"] + turnos["tarde"] + turnos["noite"]  # Soma do dia
        total_geral += total_dia  # Acumula no total geral
        # Acumula por turno
        total_turno["manha"] += turnos["manha"]
        total_turno["tarde"] += turnos["tarde"]
        total_turno["noite"] += turnos["noite"]
        dias_contados += 1

    # Calcula média por dia
    media_dia = total_geral // dias_contados
    # Calcula média por turno
    media_turno = {
        "manha": total_turno["manha"] // dias_contados,
        "tarde": total_turno["tarde"] // dias_contados,
        "noite": total_turno["noite"] // dias_contados
    }

    # Retorna todas as métricas calculadas
    return total_geral, media_dia, media_turno, total_turno

# Função para simular projeções mensais e anuais com base na produção semanal
def simular_projecoes(total_semana):
    producao_mensal = total_semana * 4  # Aproximação: 4 semanas por mês
    producao_anual = total_semana * 52  # 52 semanas por ano
    return producao_mensal, producao_anual

# Função que define a capacidade ideal mensal e anual (com 100% de eficiência)
def calcular_producao_ideal():
    capacidade_mensal_ideal = 750  # Valor fixo de referência (3 turnos)
    capacidade_anual_ideal = capacidade_mensal_ideal * 12  # Multiplicação pelos 12 meses
    return capacidade_mensal_ideal, capacidade_anual_ideal

# Função para gerar e exibir o relatório de produção completo
def emitir_relatorio(producao_semana):
    # Calcula totais e médias
    total, media_dia, media_turno, total_turno = calcular_totais(producao_semana)
    # Simula projeções
    mensal, anual = simular_projecoes(total)
    # Calcula a capacidade ideal
    ideal_mensal, ideal_anual = calcular_producao_ideal()

    # Impressão do relatório com todos os dados
    print("\n--- RELATÓRIO DE PRODUÇÃO ---\n")
    print("Produção semanal total:", total, "unidades")
    print("Média de produção por dia:", media_dia, "unidades")

    print("\nTotal de produção por turno (na semana):")
    for turno in total_turno:
        print("  ", turno, ":", total_turno[turno], "unidades")

    print("\nMédia de produção por turno (por dia):")
    for turno in media_turno:
        print("  ", turno, ":", media_turno[turno], "unidades")

    print("\n--- Projeções ---")
    print("Produção mensal estimada:", mensal, "unidades")
    print("Produção anual estimada:", anual, "unidades")

    print("\n--- Comparativo com Produção Ideal ---")
    print("Capacidade ideal mensal (3 turnos):", ideal_mensal, "unidades")
    print("Capacidade ideal anual (3 turnos):", ideal_anual, "unidades")
    print("Diferença para ideal mensal:", ideal_mensal - mensal, "unidades")
    print("Diferença para ideal anual:", ideal_anual - anual, "unidades")
    print("\n-------------------------------")

# Execução principal do programa
if __name__ == "__main__":
    producao_semana = cadastrar_producao()  # Coleta os dados de produção
    emitir_relatorio(producao_semana)  # Gera o relatório final
