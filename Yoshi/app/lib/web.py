import os
import platform
import webbrowser

# Função que executa o w3m e navega para a URL especificada (Linux)
def open_linux_webpage(url):
    os.system(f"w3m {url}")

# Função que abre o navegador padrão e navega para a URL especificada (Windows)
def open_windows_webpage(url):
    webbrowser.open(url)
