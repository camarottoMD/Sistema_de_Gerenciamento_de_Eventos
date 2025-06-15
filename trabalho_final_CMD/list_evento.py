from add_evento import *

def listar_eventos():
    
     for nome, info in eventos.items():
        print("-" * 20)
        print(f"Evento: {nome}")
        print(f"  Data: {info['data'].strftime('%d/%m/%Y')}")
        print(f"  Tema: {info['tema']}")
        print(f"  Participantes: {info['participantes']}")
        print("-" * 20)
        print(eventos)