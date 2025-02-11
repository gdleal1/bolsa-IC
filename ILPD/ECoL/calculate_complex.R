# R script for downloading necessary packages and calculating the complexity of datasets 

# Installing and loading the ECoL package
if(!require("devtools")) {
  install.packages("devtools")
}
devtools::install_github("lpfgarcia/ECoL")
library("ECoL")

# Reading dataset
datasetName <- "teste-male-discretized.csv"
datasetPath <- "C:\\Users\\gleal\\OneDrive\\Área de Trabalho\\bolsa-IC\\bolsa-IC\\ILPD\\ECoL\\datasets\\teste-male-discretized.csv"
dataset <- read.csv(datasetPath)

# Setting the target attribute
dataset$Dataset <- as.factor(dataset$Dataset)

# Calculating the complexity of the dataset and saving the results in a file
sink(file = "C:\\Users\\gleal\\OneDrive\\Área de Trabalho\\bolsa-IC\\bolsa-IC\\ILPD\\ECoL\\outputs\\outputs_complex\\output-teste-male.txt")
cat("Dataset Name:", datasetName, "\n")
cat("Number of Instances:", nrow(dataset), "\n")
cat("Number of Features:", ncol(dataset), "\n")
cat("Target attribute: Dataset\n")

cat("\nComplexity Measures:\n")
complexity_result <- ECoL::complexity(Dataset ~ ., dataset)
print(complexity_result)