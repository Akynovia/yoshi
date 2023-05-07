# Yoshi - Assistente Virtual

O projeto Yoshi é um assistente de linha de comando que permite ao usuário navegar na internet e buscar informações na Wikipedia. Ele é escrito em Python e é compatível com Windows e Linux. Ele foi desenvolvido com o intuito de ser simples e intuitivo.

# Instalação:

Para instalar as dependências necessárias, execute o arquivo install.sh no Linux ou install.bat no Windows. Certifique-se de estar no diretório raiz do projeto ao executar o arquivo de instalação.

# Como usar?
Após a instalação, execute o arquivo main.py para iniciar o assistente. Em seguida, siga as instruções na tela para navegar na internet ou buscar informações na Wikipedia.

# As seguintes opções estão disponíveis:

navegar: permite ao usuário navegar na internet. Digite o comando navegar seguido da URL que deseja acessar.
wiki: permite ao usuário pesquisar a Wikipedia. Digite o comando wiki seguido do tópico que deseja pesquisar.
limpar: limpa a tela do console.
ajuda: exibe a tela de ajuda.
sair: encerra o assistente.

# Estrutura do projeto
A estrutura do projeto é a seguinte:

# yoshi/
# ├── app/
# │   ├── main.py
# │   ├── lib/
# │   │   ├── __init__.py
# │   │   ├── help.py
# │   │   ├── web.py
# │   │   └── wikipedia.py
# │   └── tests/
# ├── config/
# │   ├── install.bat
# │   ├── install.sh
# │   └── requirements.txt
# ├── Leiame (ou morra)
# └── Readme (or die)

A pasta app contém o arquivo main.py, que é o arquivo principal do projeto, e duas subpastas:

lib, que contém os módulos Python para interação com a web e a Wikipedia, além de um arquivo __init__.py que é executado quando a subpasta é importada;
tests e um módulo Python que testa a funcionalidade do módulo web.py.
A pasta config contém arquivos de configuração e instalação do projeto:

install.bat, um script batch para instalação das dependências do projeto no Windows;
install.sh, um script shell para instalação das dependências do projeto no Linux;
requirements.txt, um arquivo que lista as dependências do projeto que devem ser instaladas com o pip.
Os arquivos Leiame e Readme (or die) são arquivos de documentação do projeto.

# Em resumo, o projeto é uma aplicação Python que permite a navegação na web e a pesquisa na Wikipedia por meio de um assistente de linha de comando. Ele é composto por módulos Python específicos, arquivos de configuração e scripts de instalação.
