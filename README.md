# Data Complexity Measures
Understanding the complexity of a dataset is fundamental to mitigating biases in machine learning models since complexity is directly related to the quality and diversity of the data, as well as the model's ability to generalize without learning biased patterns. The **data complexity measures** used in our study describe the regularities and irregularities contained in a dataset and are used to estimate the difficulty of separating instances into their expected classes. These measures were implemented in a R package called **ECoL**, divided into three groups:

**1) Featured-based measures:** Describe the level of information provided by the attributes available to distinguish the classes. Includes measures F1, F1v, F2, F3 and F4:

1. *Maximum Fisher’s discriminant ratio (F1):* Measures the separability between classes by comparing the average difference between the classes with the sum of the intra-class variances.
2. *The Directional-vector Maximum Fisher’s Discriminant Ratio (F1v):* Seeks to find a vector in the space of attributes that best separates the classes after projecting the data.
3. *Volume of overlap region (F2):* Calculates the overlap of attribute distributions within classes.
4. *Maximum Individual Feature Efficiency (F3):* Estimates the individual efficiency of each attribute in the separation of data classes. 
5. *Collective Feature Efficiency (F4):* Quantifies the number of steps needed to separate all the examples in a dataset by iteratively using the most discriminating attributes.

**2) Linearity measures:** Evaluates the feasibility of separating classes using a linear approach. Includes measures L1, L2 and L3:

1. *Sum of the Error Distance by Linear Programming (L1):* Evaluates whether the data is linearly separable by computing incorrectly classified examples for a linear threshold used in their classification.
2. *Error Rate of Linear Classifier (L2):* Measures linear separability in the original training dataset. 
3. *Non-Linearity of a Linear Classifier (L3):* Creates a new dataset by linearly interpolating pairs of examples from the same class. It uses a linear classifier trained on the original data, and its error rate is measured on the interpolated examples.

**3) Neighborhood measures:**  Characterize the presence and density of equal or different classes in local neighborhoods. Includes measures N1, N2, N3, N4, N5 and N6:

1. *Fraction of Borderline Points (N1):* Estimates the size and complexity of the class separation problem by identifying critical points in the data set, i.e., data that are very similar to each other but belong to different classes.
2. *Ratio of Intra/Extra Class Nearest Neighbor Distance (N2)*: Computes the overall distance between examples of different classes and the total distance between examples of the same class.
3. *Error Rate of the Nearest Neighbor Classifier (N3):* Evaluates the complexity of a dataset based on the error rate of a 1NN classifier.
4. *Non-Linearity of the Nearest Neighbor Classifier (N4):* Evaluates the non-linearity of a dataset based on the behavior of a NN classifier.
5. *Fraction of Hyperspheres Covering Data (T1 or N5):* Quantifies the complexity of the dataset based on how well the data can be covered by hyperspheres in feature space.
6. *Local Set Average Cardinality (LSC or N6):* Measures the local homogeneity of a dataset by calculating the average number of close neighbors belonging to the same class.

It is important to note that most of these measures vary between 0 and 1. **The closer the value is to the upper limit, the greater the complexity of the dataset analyzed.**

---
**Measures in ECoL package:**

![Screenshot from 2024-10-25 09-30-14](https://github.com/user-attachments/assets/47434638-4e4b-4edf-acf4-20952162885b)

---
 ## Packages used:
 **ECoL:** https://github.com/lpfgarcia/ECoL
 
 **ImbCoL:** https://github.com/victorhb/ImbCoL

---
## References:
[1] Arruda, J. L., Prudˆencio, R. B., and Lorena, A. C. (2020). Measuring instance hardness
using data complexity measures. In Intelligent Systems: 9th Brazilian Conference,
BRACIS 2020, Rio Grande, Brazil, October 20–23, 2020, Proceedings, Part II 9, pages
483–497. Springer.

[2] Janosi, Andras, S. W. P. M. and Detrano, R. (1989). Heart Disease. UCI Machine Learning
Repository. DOI: https://doi.org/10.24432/C52P4X.

[3] Karamizadeh, S., Abdullah, S. M., Manaf, A. A., Zamani, M., and Hooman, A. (2013).
An overview of principal component analysis. Journal of signal and information pro-
cessing, 4(3):173–175.

[4] Lorena, A. C., Garcia, L. P. F., Lehmann, J., Souto, M. C. P., and Ho, T. K. (2019).
How complex is your classification problem?: A survey on measuring classification
complexity. ACM Computing Surveys (CSUR), 52(1):1–34.

[5] Maslej, M. et al. (2022). Intersectional-Bias-Assessment. INCF. Available on inter-
net: https://training.incf.org/lesson/intersectional-approach-model-construction-and-evaluation-mental-healthcare.


[6] Rodrigues, D. D. (2023). Assessing pre-training bias in health data and estimating its
impact on machine learning algorithms.

[7] Sotoca, J. M., S´anchez, J. S., and Mollineda, R. A. (2005). A review of data complexity
measures and their applicability to pattern classification problems. Actas del III Taller
Nacional de Mineria de Datos y Aprendizaje. TAMIDA, 77.

---
## Conclusions:
https://www.canva.com/design/DAGVP26HQbw/GDpqOo9PYhn5ffnQ_vwN6A/edit?utm_content=DAGVP26HQbw&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton
