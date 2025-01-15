# Separate the main dataset into two, one with only men and the other with only women

import pandas as pd

data = pd.read_csv('datasets/heart_with_sex_column.csv')

# sex (1 = male; 0 = female)
male = data[data['sex'] == 1]
fem = data[data['sex'] == 0]

# Excluir a coluna 'sex'
male = male.drop(columns=['sex'])
fem = fem.drop(columns=['sex'])
data = data.drop(columns=['sex'])

male.to_csv('datasets/male.csv', index=False)
fem.to_csv('datasets/female.csv', index=False)
data.to_csv('datasets/heart.csv', index=False)