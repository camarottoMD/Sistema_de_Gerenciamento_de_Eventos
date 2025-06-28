from datetime import datetime
import time

"""
Vantagens de estar utilizando um dicionario global
Busca rápida: Buscar por nome é instantâneo (O(1)).
Código simples: Fácil de entender e manipular.
Compartilhamento fácil: Qualquer função ou módulo pode acessar e modificar os eventos.

-------------------------------------------------------------------------------------------------------------

Esse método é eficiente e prático para programas pequenos e médios, onde o nome do evento pode ser único.
Se precisar de nomes repetidos ou persistência, use lista de dicionários ou banco de dados.
Para a maioria dos sistemas simples, o dicionário global é a escolha mais rápida e fácil!
"""

eventos = {}

def adicionar_evento(test_mode=False):
    if test_mode:
        nome_input = "Evento Teste"
        data_input = "15/06/2025"
        hora_input = "19:30"
        tema_input = "Teste Automático"

        print(f"Preenchimento automático: {nome_input}, {data_input}, {hora_input}, {tema_input} ")
        time.sleep(1)

        """_summary_
        verificação de nome duplicado para print do erro, pois o ID dos eventos são os nomes, e o dicionario
        ja nao permite keys iguais
        """
    else:
        nome_input = input("Digite o nome do evento: ")

        nome_evento = (
        nome_input.strip().title()
    )  # Remove espaços no fim e começo e coloca a primeira letra em maiúsculo

    if nome_evento in eventos:
        print(
            f"O evento '{nome_evento}' não pode ser registrado! O nome '{nome_evento}', já esta sendo utilizado"
        )

    else:

        data_input = input("Digite a data do evento (dd/mm/aaaa): ")
        try:
            data = datetime.strptime(
                data_input,
                "%d/%m/%Y",  # -> so a aceita nesse formato
            )  # strptime = string → data / strftime = data → string    #   $d->dia em numeral     %m-> mes em numeral     %Y-> ano completo em numeral
        except ValueError:
            print("Data com valor/formato incorreto! Adicione novamente")
        
        hora_input = input("Digite a hora do evento (hh:mm): ")

        try:
            hora = datetime.strptime(hora_input, "%H:%M")
        except ValueError:
            print("Data com valor/formato incorreto! Adicione novamente")

        tema_input = input("Digite o tema do evento: ")
        tema = tema_input.strip().title()


    """
    cria o nome, faz a formatacao, e a partir disto, verifica se esse nome tem igual nos eventos
    if nome_evento in eventos: já busca só nas chaves.
    Não precisa escrever eventos.keys().
    É mais simples e mais rápido assim!
    Você não precisa especificar para o if procurar nas keys do dicionário porque, em Python, a expressão if chave in dicionario já faz a busca apenas nas chaves.
    """
    

    eventos[nome_evento] = {
        "data": data,
        "hora": hora,   #desta maneira eu não preciso percorrer as listas para remover ou editar qualquer tipo de evento
        "tema": tema,
        "participantes": [],
    }  # -> == eventos = {nome_evento: {"data": data, "tema": tema, "participantes": []}} isso seria a criacao do dic fora do def

    #tabelaLigacao =

"""
Em Python, variáveis globais (como eventos) podem ser lidas e modificadas dentro de funções, desde que você não tente reatribuir a variável (ex: eventos = {} dentro da função, o que criaria uma variável local).
Quando você faz eventos[nome_evento] = ..., você está apenas modificando o conteúdo do dicionário global, não reatribuindo ele.
"""