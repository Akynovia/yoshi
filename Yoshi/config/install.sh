#!/bin/bash

# Atualiza o gerenciador de pacotes
sudo apt-get update

# Instala o pip
sudo apt-get install -y python3-pip

# Instala o w3m
sudo apt-get install -y w3m

# Instala as dependências do pip
pip3 install wikipedia-api
