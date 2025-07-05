from func_user import participantes
from func_evento import eventos
from collections import Counter

def gerar_estatisticas_terminal():
    # estatistica de temas
    temas = [info.get('tema') for info in eventos.values() if info.get('tema')]
    temas_counter = Counter(temas)
    temas_mais_comuns = temas_counter.most_common()

    # estatistica de participantes
    participantes_ativos = [(dados.get('nome'), len(dados.get('eventos_inscrito', []))) for dados in participantes.values() if dados.get('nome')]
    participantes_ativos.sort(key=lambda x: x[1], reverse=True)

    print("\n========== ESTATÍSTICAS DO SISTEMA ==========")
    print("\nTemas de eventos mais recorrentes:")
    if temas_mais_comuns:
        for tema, count in temas_mais_comuns:
            print(f"{tema}: {count} eventos")
    else:
        print("Nenhum tema cadastrado.")

    print("\nParticipantes mais ativos:")
    if participantes_ativos:
        for nome, qtd in participantes_ativos:
            print(f"{nome}: {qtd} eventos inscritos")
    else:
        print("Nenhum participante cadastrado.")
    print("============================================\n")