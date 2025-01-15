import os
import csv

# Define o caminho para o arquivo 'output.txt'
file_path = os.path.join(os.getcwd(), 'output.txt')
# Define o caminho para o arquivo 'results.csv'
results = 'results.csv'

# Abre o arquivo 'output.txt' em modo leitura
with open(file_path, 'r') as file:
    # Abre o arquivo 'results.csv' em modo escrita com delimitador ';'
    with open(results, 'a', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=';')
        
        # Lê e escreve as quatro primeiras linhas após remover o prefixo [1]
        for _ in range(4):
            line = next(file).strip()  # Lê uma linha e remove espaços em branco extras
            if line.startswith("[1]"):
                line = line[4:]  # Remove o prefixo [1]
            writer.writerow([line])  # Escreve a linha no CSV como uma única célula
        
        # Cria uma lista para armazenar os valores numéricos
        values = []

        # Processa as linhas restantes
        for line in file:
            # Divide a linha em valores separados por espaço
            split_values = line.split()
            
            # Tenta converter cada valor em float e adicionar à lista de valores
            for value in split_values:
                try:
                    values.append(float(value))
                except ValueError:
                    continue

        # Escreve os valores numéricos no arquivo CSV
        writer.writerow(values)

# Mostra mensagem de conclusão
print("ok")
