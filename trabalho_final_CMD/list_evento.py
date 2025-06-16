from add_evento import *

def listar_eventos():
    
    for nome, info in eventos.items():
        print("-" * 20)
        print(f"Evento: {nome}")
        print(f"  Data: {info['data'].strftime('%d/%m/%Y')}") #conversao de volta para string
        print(f"  Horario: {info['hora'].strftime('%H:%M')}") #conversao de volta para string
        print(f"  Tema: {info['tema']}")
        print(f"  Participantes: {info['participantes']}")
        print("-" * 20)
        
def opcao():
    print("1 - Adicionar participante ao evento: ")
    print("2 - Buscar participante: ")