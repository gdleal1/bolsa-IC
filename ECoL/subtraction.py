# Subtracts the values of the complexity measures of the df1 dataset from the values of the df2 dataset and saves the result in a new CSV file.

NAME_DF1 = 'asian'
NAME_DF2 = 'hispanic'
import pandas as pd

df1 = pd.read_csv(f'outputs/output-{NAME_DF1}-dataset.csv')  
df2 = pd.read_csv(f'outputs/output-{NAME_DF2}-dataset.csv')  

df_result = pd.DataFrame()  
df_result['Complexity Measure'] = df1['Complexity Measure']  
df_result['Value'] = df1['Value'] - df2['Value']  

df_result.to_csv(f'outputs_sub/{NAME_DF1}-{NAME_DF2}-diff.csv', index=False)


