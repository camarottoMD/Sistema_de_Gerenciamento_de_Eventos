import uuid
import time 

participantes = dict() # == participante = {}

def adicionar_participante(test_mode=True):
    if test_mode:
        nome_user_input = "Matheus"
        id_user = uuid.uuid4()
        email_input = "user@email.com"
        prefs_input = "Gosto de IA, culinaria e Anime"

        print(f"Preenchimento automático: {nome_user_input}, {id_user}, {email_input}, {prefs_input}")
        time.sleep(3)
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
        else:
        
        verificação de id duplicado em um mesmo
        """

    nome_user = (
        nome_user_input.strip().title()
    ) 
    
    email = email_input

    prefs = prefs_input.strip().title()

    participantes[id_user] = {
        "nome": nome_user,
        "email": email,
        "prefs": prefs
        "eventos_inscrito": eventos_inscritos 
    }
    """_summary_
    preciso linkar os eventos com os participantes e vice versa, preciso mostrar quais eventos o participante esta inscrito
    """