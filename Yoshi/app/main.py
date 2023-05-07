import os
import platform
from lib.wikipedia import get_wikipedia_summary
from lib.web import open_linux_webpage, open_windows_webpage
from lib.help import show_supported_commands

# Mensagem de boas-vindas e informações sobre os comandos suportados
print("Olá! Eu sou Yoshi, seu assistente virtual. Segue abaixo os comandos que eu posso realizar:")
show_supported_commands()

# Laço principal do programa
while True:
    # Espera pela entrada do usuário
    command = input("> ").lower()

    os.system('cls' if os.name == 'nt' else 'clear')  # Limpa a tela

    # Navegar na Internet (Linux)
    if "navegar" in command and platform.system() == "Linux":
        url = input("Digite a URL a ser acessada: ")
        open_linux_webpage(url)

    # Navegar na Internet (Windows)
    elif "navegarwin" in command and platform.system() == "Windows":
        url = input("Digite a URL a ser acessada: ")
        open_windows_webpage(url)

    # Buscar informação na Wikipedia
    elif "wiki" in command:
        topic = input("Digite o tópico que deseja buscar: ")
        summary = get_wikipedia_summary(topic)
        if summary:
            print(summary)
        else:
            print("Não foi possível encontrar informações sobre o tópico especificado. Tente novamente com outra pesquisa.")

    # Comando para limpar a tela
    elif "limpar" in command:
        pass

    # Comando para exibir a tela de ajuda
    elif "ajuda" in command:
        show_supported_commands()

    # Sair do programa
    elif "sair" in command:
        print("Até mais!")
        break

    # Comando inválido
    else:
        print("Comando inválido. Por favor, digite um comando válido.")
