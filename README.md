# Medidas de complexidade de dados
A complexidade de dados pode ser medida através do tamanho do menor algoritmo necessário para descrever as relações entre os dados. Se o conjunto possuir uma certa regularidade, por exemplo, é formado um algoritmo mais compacto. Essas medidas podem ser utilizadas para estimar a dificuldade em separar os dados nas suas classes previstas.

## Palavra chaves
**1) Instances:** An instance (also known as a sample or observation) represents a single data point in the dataset. For example, in a dataset of houses, each house would be an instance, containing various attributes.

**2) Features:** Features (or attributes) are the individual measurable properties or characteristics of an instance. In the house dataset, features could include the number of bedrooms, square footage, price, location, etc. Features are used as inputs for machine learning models.

**3) Classes:** Classes (or labels) refer to the categories or outcomes that instances can belong to, particularly in classification tasks. For example, if the dataset is for predicting whether a house is "expensive" or "affordable," those two categories would be the classes.

**4) Overlap:** Refers to the degree to which different classes or categories share similar feature values. High class overlap can lead to misclassification, as the model may incorrectly assign an instance to the wrong class based on its features.

**5) Boundary:** Represents the regions in the feature space where instances from different classes meet, and, conceptually, it’s where classification is most challenging.

# Medidas ECoL

Essas métricas descrevem as regularidades e irregularidades contidas no conjunto de dados. Quanto mais os valores das métricas aumentam, maior a complexidade do conjunto de dados analisado:

**1) Featured-based measures:** Caracterizam o quão informativos são os atributos disponíveis para separar as classes

1. *Maximum Fisher’s discriminant ratio (F1):* Compara a diferença entre as classes de dados com a soma das variancias delas. Ajuda a detectar um atributo chamado discriminativo, o qual consegue distinguir melhor as classes de dados. Quanto maior ele for, mais parecidas são as classes.
2. *Volume of overlap region (F2):* Calcula a sobreposição das distribuições dos atributos dentro das classes. Faz isso calculando os valores máximo e mínimo de cada atributo dentro de uma classe e também da região de sobreposição entre as classes. Quanto maior ele for, então maior a sobreposição entre as classes.
3. *Maximum Individual Feature Efficiency (F3):* Estima a eficiência individual de cada atributo em separar as classes de dados. Permite identificar o atributo que mostra menos overlap entre classes diferentes.
4. *Collective Feature Efficiency (F4):* Através do atributo mais discriminativo, obtido por F3, separa e retira do dataset todos os exemplos que podem ser distinguidos por ele. Esse processo é repetido até todos os atributos serem considerados ou não existirem mais exemplos a separar. Essa medida indica quantos passos são necessários para discriminar todos os exemplos. Logo, quanto menor for essa medida, um maior número de exemplos podem ser discriminados e, consequentemente, o problema é mais simples. 

**2) Linearity measures:** Tentar quantificar se as classes podem ser separadas linearmente

1. *Sum of the Error Distance by Linear Programming (L1):* Avalia se os dados são linearmente separáveis computando exemplos classificados incorretamente para um limite linear usado em sua classificação. Quanto menor for L1, então
o problema pode ser considerado mais simples e linearmente separável.
2. *Error Rate of Linear Classifier (L2):* Mede a separabilidade linear no dataset de treinamento original. Valores altos de L2 denotam mais erros ao separar os dados em suas classes, correspondendo a uma grande complexidade.

**3) Neighborhood measures:** Caracterizam a presença e a densidade de classes iguais (overlap) ou diferentes nas vizinhanças locais

1. *Fraction of Borderline Points (N1):* Estima o tamanho e a complexidade do problema de separação de classes através da identificação de pontos críticos no dataset, isto é, dados que são muito parecidos entre eles mas pertencentes
a classes diferentes. Valores altos indicam complexidade maior.
2. *Ratio of Intra/Extra Class Nearest Neighbor Distance (N2)*: Computa a distância geral entre exemplos de classes diferentes e a distância total entre exemplos da mesma classe. Se o valor de N2 for baixo, menor a complexidade e maior a distância entre exemplos de classes diferentes em relação a distância entre exemplos da mesma classe.
3. *Error Rate of the Nearest Neighbor Classifier (N3):* Maiores valores de N3 indicam que muitas instâncias são próximas de instâncias de outras classes.
4. *Non-Linearity of the Nearest Neighbor Classifier (N4):* Similar a medida L3. Quanto maior, mais complexo o dataset.

**4) Network measures:** Extraem informações estruturais do conjunto de dados, modelando-o como um grafo

**5) Dimensionality measures:** Avaliam a esparsidade dos dados com base no número de amostras relativas à dimensionalidade dos dados

**6) Class imbalance measures:** Considera a proporção do número de exemplos entre as classes

---
**Measures in ECoL package:**

![Screenshot from 2024-10-25 09-30-14](https://github.com/user-attachments/assets/47434638-4e4b-4edf-acf4-20952162885b)

---
 ## Pacotes utilizados:
 **ECoL:** https://github.com/lpfgarcia/ECoL
 
 **ImbCoL:** https://github.com/victorhb/ImbCoL

---
 ## Artigos / Textos:
**Paper Lorena:**: https://arxiv.org/pdf/1808.03591

**Bernouini**: https://rachidbenouini.medium.com/data-complexity-measures-8313e349c7a5

---
## Conclusões:
**Link apresentação:**
https://www.canva.com/design/DAGVP26HQbw/GDpqOo9PYhn5ffnQ_vwN6A/edit?utm_content=DAGVP26HQbw&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton
