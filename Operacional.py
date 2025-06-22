# Aluno:Rodrigo Costa

def cadastrar_producao():
    print("\nCadastro da produção diária (manhã, tarde, noite):\n")
    dias = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]
    turnos = ["manha", "tarde", "noite"]
    producao_semana = {}

    for dia in dias:
        producao_semana[dia] = {}
        for turno in turnos:
            while True:
                try:
                    valor = int(input(f"Informe a produção para {dia} - {turno}: "))
                    producao_semana[dia][turno] = valor
                    break
                except ValueError:
                    print("Digite um número válido!")
    return producao_semana

def calcular_totais(producao_semana):
    total_geral = 0
    total_turno = {"manha": 0, "tarde": 0, "noite": 0}
    dias_contados = 0

    for dia in producao_semana:
        turnos = producao_semana[dia]
        total_dia = turnos["manha"] + turnos["tarde"] + turnos["noite"]
        total_geral += total_dia
        total_turno["manha"] += turnos["manha"]
        total_turno["tarde"] += turnos["tarde"]
        total_turno["noite"] += turnos["noite"]
        dias_contados += 1

    media_dia = total_geral // dias_contados
    media_turno = {
        "manha": total_turno["manha"] // dias_contados,
        "tarde": total_turno["tarde"] // dias_contados,
        "noite": total_turno["noite"] // dias_contados
    }

    return total_geral, media_dia, media_turno, total_turno

def simular_projecoes(total_semana):
    producao_mensal = total_semana * 4
    producao_anual = total_semana * 52
    return producao_mensal, producao_anual

def calcular_producao_ideal():
    capacidade_mensal_ideal = 750  # Considerando 3 turnos
    capacidade_anual_ideal = capacidade_mensal_ideal * 12
    return capacidade_mensal_ideal, capacidade_anual_ideal

def emitir_relatorio(producao_semana):
    total, media_dia, media_turno, total_turno = calcular_totais(producao_semana)
    mensal, anual = simular_projecoes(total)
    ideal_mensal, ideal_anual = calcular_producao_ideal()

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

if __name__ == "__main__":
    producao_semana = cadastrar_producao()
    emitir_relatorio(producao_semana)