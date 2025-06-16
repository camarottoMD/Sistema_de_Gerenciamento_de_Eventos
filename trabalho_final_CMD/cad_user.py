from list_evento import *
from add_evento import *
import uuid

participante = dict() # == participante = {}

def adicionar_evento(test_mode=True):
    if test_mode:
        nome_user_input = "Matheus"
        id_user = uuid.uuid4()
        email_input = "user@email.com"
        prefs_input = "Gosto de IA, culinaria e Anime"

        print(f"Preenchimento automático: {nome_user_input}, {id_user}, {email_input}, {prefs_input}")
    else:
        nome_user_input = input("Digite o seu nome completo: ")
        id_user = uuid.uuid4()
        email_input = input("Digite o seu email: ")
        prefs_input = input("Digite suas preferencias sobre temas de eventos: ")

        """for nome in participante[nome].keys():
        if nome_user_input == nome:
            print(
                f"O usuario '{nome}' não pode ser registrado! O nome '{nome}', já esta sendo utilizado"
            )
        else:"""
        """_summary_
        verificação de nome duplicado para print do erro, pois o ID dos eventos são os nomes, e o dicionario
        ja nao permite keys iguais
        """

    nome_user = (
        nome_user_input.strip().title()
    ) 
    
    email = email_input

    prefs = prefs_input.strip().title()

    participantes[id_user] = {
        "nome": nome,
        "email": email,
        "prefs": prefs
    }