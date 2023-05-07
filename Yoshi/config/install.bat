@echo off
echo Atualizando o pip...
python -m pip install --upgrade pip

echo Instalando os requisitos...
python -m pip install -r requirements

echo Instalação concluída!
pause
