# Create datasets for experiments, separing them acording to a sensitive attribute
import pandas as pd

original_dataset = pd.read_csv('datasets/intersectional-bias-reduced.csv')

# Separate the main dataset into two, according to the sex attribute
male_reduced = original_dataset[original_dataset['Sex'] == 'Male']
female_reduced = original_dataset[original_dataset['Sex'] == 'Female']

# Remove the Sex column of the datasets
male_reduced = male_reduced.drop(columns=['Sex'])
female_reduced = female_reduced.drop(columns=['Sex'])

# Save the datasets
male_reduced.to_csv('datasets/male-reduced.csv', index=False)
female_reduced.to_csv('datasets/female-reduced.csv', index=False)