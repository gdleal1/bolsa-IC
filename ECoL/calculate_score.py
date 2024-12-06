# Calculates a score for each complexity measure group
import pandas as pd

# Calculates the average magnitude of the variation in the group.
def mean_absolute(data):
    return data['Value'].abs().mean()

# Calculates the highest individual value in the group
def max_absolute(data):
    return data['Value'].abs().max()

# Calculates the standard deviation of the group
def std_dev(data):
    return data['Value'].std()

# Calculates the score for the group
def score(data):
    return round((mean_absolute(data) + max_absolute(data) + std_dev(data)),2)

NAME_OUTPUT = 'white'
output_path = f'outputs_complex/output-{NAME_OUTPUT}.csv'  
data = pd.read_csv(output_path)

# Feature-Based Measures
F_measures = data.iloc[0:5]

# Neighborhood Measures
N_measures = data.iloc[5:11]

# Linearity Measures
L_measures = data.iloc[11:14]

with open(f'scores/score-{NAME_OUTPUT}-output.txt', 'w') as f:
    f.write("Score for Feature-Based Measures: " + str(score(F_measures)) + "\n")
    f.write("Score for Neighborhood Measures: " + str(score(N_measures)) + "\n")
    f.write("Score for Linearity Measures: " + str(score(L_measures)) + "\n")


