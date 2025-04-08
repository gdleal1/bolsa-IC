# R script for downloading necessary packages and calculating the complexity of datasets 

# Installing and loading the ECoL package
if(!require("devtools")) {
  install.packages("devtools")
}
devtools::install_github("lpfgarcia/ECoL")
library("ECoL")

# Reading dataset
datasetName <- "female-Un.csv"
datasetPath <- "/home/gabriel/Documents/bolsa-IC/bolsa-IC/Diabetes/ECoL/datasets/female-Un.csv"
dataset <- read.csv(datasetPath)

# Setting the target attribute
dataset$Diabetes_binary <- as.factor(dataset$Diabetes_binary)

# Calculating the complexity of the dataset and saving the results in a file
sink(file = "/home/gabriel/Documents/bolsa-IC/bolsa-IC/Diabetes/ECoL/outputs/outputs_complex/output-female-Un.txt")
cat("Dataset Name:", datasetName, "\n")
cat("Number of Instances:", nrow(dataset), "\n")
cat("Number of Features:", ncol(dataset), "\n")
cat("Target attribute: Diabetes_binary\n")

cat("\nComplexity Measures:\n")
complexity_result <- ECoL::complexity(Diabetes_binary ~ ., dataset)
print(complexity_result)