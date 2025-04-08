# Reduce a dataset to a smaller size while maintaining the proportions of predetermined attributes attributes

import pandas as pd
from sklearn.model_selection import train_test_split


df = pd.read_csv("datasets/diabetes-original-Un.csv")

# Group by two attributes 
grouped = df.groupby(['Diabetes_binary', 'Sex'])

# Set desired size for the reduced dataset
desired_size = 12000  

# Calculate the proportion of each group in the original dataset
group_sizes = grouped.size()
total_size = group_sizes.sum()

# Calculate the sample size for each group based on the desired size
group_sample_sizes = (group_sizes / total_size) * desired_size

# Perform stratified sampling
sampled_df = grouped.apply(
    lambda x: x.sample(n=int(group_sample_sizes.loc[x.name]), random_state=42)
)

# Reset the index of the resulting sampled dataframe
sampled_df = sampled_df.reset_index(drop=True)

# Save the sampled dataset
sampled_df.to_csv('datasets/diabetes-reduced-Un.csv', index=False)


print("\n==================== Proporções nos datasets ====================\n")
print("\n------------------ ORIGINAL ------------------")
combinacoes_originais = df[['Diabetes_binary', 'Sex']].value_counts(normalize=True) * 100
print(combinacoes_originais.sort_index())
"""porcentagem_diabetes = df['Diabetes_binary'].value_counts(normalize=True) * 100
print("\nPorcentagem de Diabetes_binary:")
print(porcentagem_diabetes)

porcentagem_sex = df['Sex'].value_counts(normalize=True) * 100
print("\nPorcentagem de Sex:")
print(porcentagem_sex)"""


print("\n------------------ REDUZIDO ------------------")
combinacoes_reduzidas = sampled_df[['Diabetes_binary', 'Sex']].value_counts(normalize=True) * 100
print(combinacoes_reduzidas.sort_index())
"""porcentagem_diabetes = sampled_df['Diabetes_binary'].value_counts(normalize=True) * 100
print("\nPorcentagem de Diabetes_binary:")
print(porcentagem_diabetes)

porcentagem_sex = sampled_df['Sex'].value_counts(normalize=True) * 100
print("\nPorcentagem de Sex:")
print(porcentagem_sex)"""
