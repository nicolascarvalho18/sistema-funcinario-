import os
import csv
import pandas as pd
import shutil

# Função para garantir que o diretório de pagamentos exista
def ensure_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

# Função para registrar os dados de um funcionário
def registrar_funcionario(nome, email, pix, dias_trabalhados, caminho_comprovante):
    # Definir o nome do arquivo CSV
    arquivo_csv = 'funcionarios.csv'
    
    # Verificar se o arquivo CSV já existe
    if not os.path.isfile(arquivo_csv):
        # Se não existir, criar o arquivo e adicionar o cabeçalho
        with open(arquivo_csv, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Nome', 'Email', 'Pix', 'Dias Trabalhados', 'Comprovante Pagamento'])
    
    # Adicionar os dados do funcionário ao arquivo CSV
    nome_arquivo_comprovante = os.path.basename(caminho_comprovante)
    with open(arquivo_csv, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([nome, email, pix, dias_trabalhados, nome_arquivo_comprovante])
    
    # Salvar o comprovante de pagamento na pasta
    pasta_pagamentos = 'comprovantes_pagamento'
    ensure_directory(pasta_pagamentos)
    shutil.copy(caminho_comprovante, os.path.join(pasta_pagamentos, nome_arquivo_comprovante))

# Função para visualizar os dados dos funcionários
def visualizar_funcionarios():
    arquivo_csv = 'funcionarios.csv'
    if os.path.isfile(arquivo_csv):
        df = pd.read_csv(arquivo_csv)
        print(df)
    else:
        print("Nenhum dado encontrado.")

# Exemplo de uso
registrar_funcionario(
    nome="João Silva",
    email="joao.silva@example.com",
    pix="123456789",
    dias_trabalhados=20,
    caminho_comprovante="caminho/para/joao_silva_comprovante.jpg"
)

registrar_funcionario(
    nome="Maria Oliveira",
    email="maria.oliveira@example.com",
    pix="987654321",
    dias_trabalhados=22,
    caminho_comprovante="caminho/para/maria_oliveira_comprovante.png"
)

# Visualizar dados dos funcionários
visualizar_funcionarios()
