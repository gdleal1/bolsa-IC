# Medidas de complexidade de dados
A complexidade de dados pode ser medida através do tamanho do menor algoritmo necessário para descrever as relações entre os dados. Se o conjunto possuir uma certa regularidade, por exemplo, é formado um algoritmo mais compacto. Essas medidas podem ser utilizadas para estimar a dificuldade em separar os dados nas suas classes previstas.

## Palavra chaves
**1) Instances:** An instance (also known as a sample or observation) represents a single data point in the dataset. For example, in a dataset of houses, each house would be an instance, containing various attributes.

**2) Features:** Features (or attributes) are the individual measurable properties or characteristics of an instance. In the house dataset, features could include the number of bedrooms, square footage, price, location, etc. Features are used as inputs for machine learning models.

**3) Classes:** Classes (or labels) refer to the categories or outcomes that instances can belong to, particularly in classification tasks. For example, if the dataset is for predicting whether a house is "expensive" or "affordable," those two categories would be the classes.

**4) Overlap:** Refers to the degree to which different classes or categories share similar feature values. High class overlap can lead to misclassification, as the model may incorrectly assign an instance to the wrong class based on its features.

# Medidas ECoL

Essas métricas descrevem as regularidades e irregularidades contidas no conjunto de dados:

**1) Featured-based measures:** Caracterizam o quão informativos são os atributos disponíveis para separar as classes

1. *Maximum Fisher’s discriminant ratio (F1):* Compara a diferença entre as classes de dados com a soma das variancias delas. Ajuda a detectar um atributo chamado discriminativo, o qual consegue distinguir melhor as classes de dados. Quanto maior ele for, mais parecidas são as classes.
2. *Volume of overlap region (F2):* Calcula a sobreposição das distribuições dos atributos dentro das classes. Faz isso calculando os valores máximo e mínimo de cada atributo dentro de uma classe e também da região de sobreposição entre as classes. Quanto maior ele for, então maior a sobreposição entre as classes.
3. *Maximum Individual Feature Efficiency (F3):* Estima a eficiência individual de cada atributo em separar as classes de dados. Permite identificar o atributo que mostra menos overlap entre classes diferentes.
4. *Collective Feature Efficiency (F4):* Através do atributo mais discriminativo, obtido por F3, separa e retira do dataset todos os exemplos que podem ser distinguidos por ele. Esse processo é repetido até todos os atributos serem considerados ou não existirem mais exemplos a separar. Essa medida indica quantos passos são necessários para discriminar todos os exemplos. Logo, quanto menor for essa medida, um maior número de exemplos podem ser discriminados e, consequentemente, o problema é mais simples. 



**2) Linearity measures:** Tentar quantificar se as classes podem ser separadas linearmente

**3) Neighborhood measures:** Caracterizam a presença e a densidade de classes iguais ou diferentes nas vizinhanças locais

**4) Network measures:** Extraem informações estruturais do conjunto de dados, modelando-o como um grafo

**5) Dimensionality measures:** Avaliam a esparsidade dos dados com base no número de amostras relativas à dimensionalidade dos dados

**6) Class imbalance measures:** Considera a proporção do número de exemplos entre as classes

----
 ## Pacotes utilizados:
 **ECoL:** https://github.com/lpfgarcia/ECoL
 
 **ImbCoL:** https://github.com/victorhb/ImbCoL

---
 ## Artigos / Textos:
**Paper Lorena:**: https://arxiv.org/pdf/1808.03591

**Bernouini**: https://rachidbenouini.medium.com/data-complexity-measures-8313e349c7a5
 

