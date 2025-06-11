from add_evento import *

def listar_eventos():
    #print(eventos.items())
     for nome, info in eventos.items():
        print("-" * 20)
        print(f"Evento: {nome}")
        print(f"  Data: {info['data'].strftime('%d/%m/%Y')}")
        print(f"  Tema: {info['tema']}")
        print(f"  Participantes: {info['participantes']}")
        print("-" * 20)