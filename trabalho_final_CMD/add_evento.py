from datetime import datetime

eventos = {}

def adicionar_evento(eventos, test_mode = True):

    if test_mode:
        nome_input = "Evento Teste"
        data_input = "15/06/2025"
        tema_input = "Teste Automático"
        hora_input = "19:30"

        print(f"Preenchimento automático: {nome_input}, {data_input}, {tema_input}")
    else: 
        nome_input= input("Digite o nome do evento: ")
        data_input = input("Digite a data do evento (dd/mm/aaaa): ")
        hora_input = input("Digite a hora do evento (hh:mm): ")
        tema_input = input("Digite o tema do evento: ")
    """
    fazer a verificacao para voltar a mensagem de erro e retornar pros inputs. tentar fazer alguma coisa pra que ele saiba que na hora do dic salvar, e o result for none por ja existir outro com a mesma chave, ai ele da o resultado e volta uma mensagem de erro
    """
    if nome_input == eventos[nome]: 
        print("Já tem esse nome")
        adicionar_evento()
    else:
        """_summary_
        verificação de nome duplicado para print do erro, pois o ID dos eventos são os nomes, e o dicionario
        ja nao permite keys iguais
        """

        nome_evento = (
            nome_input.strip().title()
        )  # Remove espaços no fim e começo e coloca a primeira letra em maiúsculo

        # fazer tratamento de id de evento, porem se for fazer com banco ta de boa
        
        data = datetime.strptime(
            data_input,
            "%D/%m/%Y" #-> so a aceita nesse formato
        )  # strptime = string → data / strftime = data → string    #   $d->dia em numeral     %m-> mes em numeral     %Y-> ano completo em numeral

        hora = datetime.strptime(
            hora_input,
            "%H:%M"
        )
        
        tema = tema_input.strip().title()

        eventos[nome_evento] = {
            "data": data,
            "tema": tema,
            "participantes": [],
        }  # -> == eventos = {nome_evento: {"data": data, "tema": tema, "participantes": []}} isso seria a criacao do dic fora do def

