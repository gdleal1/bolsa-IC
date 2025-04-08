# Create datasets for experiments, separing them acording to a sensitive attribute
import pandas as pd

original_dataset = pd.read_csv('datasets/diabetes-reduced-Un.csv')

# Separate the original dataset  according to a sensitive attribute
male_dataset= original_dataset[original_dataset['Sex'] == 1]
female_dataset = original_dataset[original_dataset['Sex'] == 0]

# Remove the sensitive attribute column of the datasets
male_dataset = male_dataset.drop(columns=['Sex'])
female_dataset = female_dataset.drop(columns=['Sex'])

# Save the datasets
male_dataset.to_csv('datasets/male-Un.csv', index=False)
female_dataset.to_csv('datasets/female-Un.csv', index=False)