# Create a graphic with the complexity measures for a dataset

import pandas as pd
import matplotlib.pyplot as plt

NAME_DS1 = 'asian'
NAME_DS2 = 'hispanic'
TITLE = f'Difference between the complexity measures of the {NAME_DS1} and {NAME_DS2} datasets'


def create():
    
    file_path = f'outputs_sub/{NAME_DS1}-{NAME_DS2}-diff.csv'  
    data = pd.read_csv(file_path)

    # Different colors for positive and negative values
    colors = ['cornflowerblue' if value > 0 else 'lightcoral' for value in data['Value']]

    # Bar graphic
    plt.figure(figsize=(10, 6))
    plt.bar(data['Complexity Measure'], data['Value'], color=colors)

    # Line graphic
    plt.plot(data['Complexity Measure'], data['Value'], color='darkorange', label='Linha')

    plt.title(TITLE)
    plt.xlabel('Complexity Measure')
    plt.ylabel('Value')
    plt.xticks(rotation=45)  
    plt.tight_layout()  

    graphic_path = f"graphics/{NAME_DS1}_{NAME_DS2}_diff_graphic.png"
    plt.savefig(graphic_path, dpi=300)

if __name__ == "__main__":
    create()
