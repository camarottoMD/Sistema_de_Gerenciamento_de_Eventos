import os
import func_evento
import func_user
import menu_evento
from time import sleep

"""
limpa a tela do terminal, compatível com Windows e Unix.
"""
def limpar_tela():
    os.system("cls" if os.name == 'nt' else 'clear')

def menu():
    limpar_tela()
    while True:
        try:
            print("1 - Listagem de Eventos")
            print("2 - Adicionar Evento")
            print("3 - Remover Evento")
            print("4 - Estatísticas do Sistema")
            print("5 - Sair")
            escolhaOp = input("Selecione um número correspondente as opções acima: ")
            if not escolhaOp.isdigit():
                print("Por favor, digite um número válido.")
                sleep(2)
                limpar_tela()
                continue
            escolhaOp = int(escolhaOp)
            opcaoMenu(escolhaOp)
            break
        except Exception as e:
            print(f"Erro no menu: {e}")
            sleep(2)


def opcaoMenu(escolhaOp):
    limpar_tela()
    try:
        from estatisticas import gerar_estatisticas_terminal
        match escolhaOp:
            case 1:
                if not func_evento.eventos:
                    print("Nenhum evento cadastrado!")
                    sleep(2)
                    menu()
                    return
                func_evento.listar_eventos()
                Menu_List()
            case 2:
                try:
                    func_evento.adicionar_evento()
                except Exception as e:
                    print(f"Erro ao adicionar evento: {e}")
                    sleep(2)
                menu()
            case 3:
                try:
                    func_evento.remover_evento()
                except Exception as e:
                    print(f"Erro ao remover evento: {e}")
                    sleep(2)
                sleep(2)
                menu()
            case 4:
                gerar_estatisticas_terminal()
                input("Pressione Enter para voltar ao menu...")
                menu()
            case 5:
                exit()
            case _:
                print("Opção não válida!")
                sleep(2)
                menu()
                print("-" * 20)
    except Exception as e:
        print(f"Erro ao selecionar opção do menu: {e}")
        sleep(2)
        menu()


def Menu_List():
    while True:
        try:
            print("-" * 20)
            print("1 - Buscar participante: ")
            print("2 - Escolha um evento: ")
            print("3 - Listar temas de eventos: ")
            print("4 - Voltar: ")

            opcao = input("Selecione um número correspondente as opções acima: ")
            if not opcao.isdigit():
                print("Por favor, digite um número válido.")
                sleep(2)
                limpar_tela()
                continue
            opcao = int(opcao)
            print("-" * 20)

            match opcao:
                case 1:
                    try:
                        func_user.buscarParticipante()
                    except Exception as e:
                        print(f"Erro ao buscar participante: {e}")
                        sleep(2)
                case 2:
                    try:
                        escolhaEvento()
                    except Exception as e:
                        print(f"Erro ao escolher evento: {e}")
                        sleep(2)
                case 3:
                    try:
                        func_evento.listar_temas()
                    except Exception as e:
                        print(f"Erro ao listar temas: {e}")
                        sleep(2)
                case 4:
                    break
                case _:
                    print("Opção inválida")
                    sleep(2)
        except Exception as e:
            print(f"Erro no Menu_List: {e}")
            sleep(2)

def escolhaEvento():
    limpar_tela()
    try:
        while True:
            nome_evento = input("Escreva o nome do evento que você deseja visualizar: ").strip().title()
            if not nome_evento:
                print("Nome do evento não pode ser vazio!")
                sleep(2)
                continue
            if nome_evento in func_evento.eventos:
                try:
                    menu_evento.menuEvento(nome_evento)
                except Exception as e:
                    print(f"Erro ao abrir menu do evento: {e}")
                    sleep(2)
                break
            else:
                print("Esse evento não existe!")
                sleep(2)
        return nome_evento
    except Exception as e:
        print(f"Erro ao escolher evento: {e}")
        sleep(2)