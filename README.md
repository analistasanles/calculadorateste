# calculadorateste
atividade calculadora ebac. código Python com script de execução em Shell
# Calculadora Python

Este repositório contém um código Python para uma **calculadora simples** que realiza operações matemáticas básicas. A calculadora foi desenvolvida para receber dois números do usuário e realizar uma das seguintes operações:
- Soma
- Subtração
- Multiplicação
- Divisão
Calculadora
Este repositório contém um código em Python para uma calculadora simples que realiza operações básicas de adição, subtração, multiplicação e divisão, e um arquivo shell script (calculadora.sh) para facilitar a execução do código Python.

Como Executar
1. Clonar o Repositório
Primeiro, clone este repositório para o seu computador:

bash

git clone https://github.com/analistasanles/calculadora.git
2. Navegar até o Diretório
Depois de clonar, entre no diretório onde o repositório foi salvo:

bash

cd caminho/para/seu/repositório
3. Criar e Editar o Arquivo calculadora.sh
Crie o arquivo shell script com o seguinte comando:

bash

nano calculadora.sh
Isso abrirá o editor de texto nano. Dentro do arquivo, cole o seguinte código:

bash

#!/bin/bash
# Script para executar a calculadora Python
python3 calculadora.py
4. Tornar o Script Executável
Você precisará alterar as permissões para garantir que o arquivo seja executável. Execute o seguinte comando:

bash

chmod +x calculadora.sh
Isso permite que você execute o arquivo como um script.

5. Definir Permissões de Acesso
Para garantir que apenas o proprietário do arquivo tenha permissão de escrita e outros usuários tenham apenas permissão de leitura, use:

bash

chmod 744 calculadora.sh
6. Executar o Script
Agora você pode rodar o script para executar a calculadora Python com o seguinte comando:

bash

./calculadora.sh
Requisitos
Python 3.10 ou superior

Terminal (Linux/Mac) ou Git Bash (no Windows)

Observação
Certifique-se de que o Python 3 esteja instalado na sua máquina. Se não estiver, você pode instalá-lo com o comando:

bash
sudo apt-get install python3

## Como executar o arquivo `.sh`

Caso você tenha um arquivo de shell script (`.sh`) que automatiza a execução do código Python, siga as instruções abaixo para rodá-lo:

### Passo 1: Dar permissão de execução ao arquivo `.sh`

Primeiro, é necessário garantir que o arquivo `.sh` tenha permissão de execução. No terminal, navegue até o diretório onde o arquivo `.sh` está localizado e execute o seguinte comando:

```bash
chmod +x nome_do_arquivo.sh

PARA EXECUTAR:
python3 --version
sudo apt update
sudo apt install python3
python3 calculadora.py

