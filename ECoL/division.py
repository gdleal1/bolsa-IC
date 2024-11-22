NAME_DF1 = 'white'
NAME_DF2 = 'nonWhite'
import pandas as pd

df1 = pd.read_csv(f'outputs/output-{NAME_DF1}.csv').head(14)  
df2 = pd.read_csv(f'outputs_sub/{NAME_DF2}-{NAME_DF1}-diff.csv').head(14)  

df_result = pd.DataFrame()  
df_result['Complexity Measure'] = df1['Complexity Measure']  
df_result['Increase (%)'] = df2['Value'] / df1['Value'] * 100

df_result.to_csv(f'outputs_div/{NAME_DF2}-{NAME_DF1}-increase.csv', index=False)


