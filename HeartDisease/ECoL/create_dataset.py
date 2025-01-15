# Create datasets for experiments, separing them acording to a sensitive attribute
import pandas as pd

original_dataset = pd.read_csv('datasets/heart-disease.csv')

# Eliminate missing values
original_dataset['thal'] = original_dataset['thal'].replace('?', 0.0).astype(float)
original_dataset['ca'] = original_dataset['ca'].replace('?', 4.0).astype(float)

# Transform all columns in integers
original_dataset = original_dataset.astype(int)

# Separate the original dataset  according to a sensitive attribute
male_dataset= original_dataset[original_dataset['sex'] == 1]
female_dataset = original_dataset[original_dataset['sex'] == 0]
adult_dataset = original_dataset[(original_dataset['age'] >= 29) & (original_dataset['age'] <= 59)]
elderly_dataset = original_dataset[original_dataset['age'] >= 60]

# Remove the sensitive attribute column of the datasets
male_dataset = male_dataset.drop(columns=['sex'])
female_dataset = female_dataset.drop(columns=['sex'])
adult_dataset = adult_dataset.drop(columns=['age'])
elderly_dataset = elderly_dataset.drop(columns=['age'])

# Save the datasets
male_dataset.to_csv('datasets/male-discretized.csv', index=False)
female_dataset.to_csv('datasets/female-discretized.csv', index=False)
adult_dataset.to_csv('datasets/adult-discretized.csv', index=False)
elderly_dataset.to_csv('datasets/elderly-discretized.csv', index=False)
original_dataset.to_csv('datasets/heart-disease-discretized.csv',index=False)



