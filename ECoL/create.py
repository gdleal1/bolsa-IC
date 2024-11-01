# Create datasets for experiments, separing them acording to a sensitive attribute
import pandas as pd

original_dataset = pd.read_csv('datasets/intersectional-bias-reduced.csv')

# Separate the main dataset  according to the sensitive attribute
male_reduced = original_dataset[original_dataset['Sex'] == 'Male']
female_reduced = original_dataset[original_dataset['Sex'] == 'Female']
asian_reduced = original_dataset[original_dataset['Race'] == 'Asian']
black_reduced = original_dataset[original_dataset['Race'] == 'Black']
white_reduced = original_dataset[original_dataset['Race'] == 'White']
hispanic_reduced = original_dataset[original_dataset['Race'] == 'Hispanic']



# Remove the sensitive attribute column of the datasets
male_reduced = male_reduced.drop(columns=['Sex'])
female_reduced = female_reduced.drop(columns=['Sex'])
asian_reduced = asian_reduced.drop(columns=['Race'])
black_reduced = black_reduced.drop(columns=['Race'])
white_reduced = white_reduced.drop(columns=['Race'])
hispanic_reduced = hispanic_reduced.drop(columns=['Race'])

# Save the datasets
male_reduced.to_csv('datasets/male-reduced.csv', index=False)
female_reduced.to_csv('datasets/female-reduced.csv', index=False)
asian_reduced.to_csv('datasets/asian-reduced.csv', index=False)
black_reduced.to_csv('datasets/black-reduced.csv', index=False)
white_reduced.to_csv('datasets/white-reduced.csv', index=False)
hispanic_reduced.to_csv('datasets/hispanic-reduced.csv', index=False)
