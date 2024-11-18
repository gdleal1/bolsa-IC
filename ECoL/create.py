# Create datasets for experiments, separing them acording to a sensitive attribute
import pandas as pd

def discretize_sex(x):
    if x == 'Female':
        return 0
    elif x == 'Male':
        return 1
    else:
        raise

def discretize_race(x):
    if x == 'White':
        return 1
    else:
        return 0
    
def discretize_housing(x):
    if x == 'Stable':
        return 0
    elif x == 'Unstable':
        return 1
    else:
        raise

def discretize_delay(x):
    if x == 'No':
        return 0
    elif x == 'Yes':
        return 1
    else:
        raise

# Discretize the non-numeric columns of the dataset
original_dataset = pd.read_csv('datasets/intersectional-bias.csv')
original_dataset['Sex'] = original_dataset['Sex'].apply(lambda x: discretize_sex(x))
original_dataset['Race'] = original_dataset['Race'].apply(lambda x: discretize_race(x))
original_dataset['Housing'] = original_dataset['Housing'].apply(lambda x: discretize_housing(x))
original_dataset['Delay'] = original_dataset['Delay'].apply(lambda x: discretize_delay(x))

# Separate the main dataset  according to the sensitive attribute
male_dataset= original_dataset[original_dataset['Sex'] == 1]
female_dataset = original_dataset[original_dataset['Sex'] == 0]
nonWhite_dataset = original_dataset[original_dataset['Race'] == 0]
white_dataset = original_dataset[original_dataset['Race'] == 1]

# Remove the sensitive attribute column of the datasets
male_dataset = male_dataset.drop(columns=['Sex'])
female_dataset = female_dataset.drop(columns=['Sex'])
white_dataset = white_dataset.drop(columns=['Race'])
nonWhite_dataset = nonWhite_dataset.drop(columns=['Race'])


# Save the datasets
male_dataset.to_csv('datasets/male-discretized.csv', index=False)
female_dataset.to_csv('datasets/female-discretized.csv', index=False)
white_dataset.to_csv('datasets/white-discretized.csv', index=False)
nonWhite_dataset.to_csv('datasets/nonWhite-discretized.csv', index=False)
original_dataset.to_csv('datasets/intersectional-bias-discretized.csv', index=False)

