import pandas as pd

# Defina os dados como string (ou carregue de um arquivo CSV)
data = "bolsa-IC\HeartDisease\ECoL\datasets\heart-disease.csv"

# Transforme os dados em um DataFrame
df = pd.read_csv(data)

# Encontre o menor e o maior valor da coluna "age"
min_age = df['age'].min()
max_age = df['age'].max()

print(f"Menor idade: {min_age}")
print(f"Maior idade: {max_age}")
