# R script for downloading necessary packages and calculating the complexity of datasets 

# Installing and loading the ECoL package
if(!require("devtools")) {
  install.packages("devtools")
}
devtools::install_github("lpfgarcia/ECoL")
library("ECoL")

# Reading dataset
datasetName <- "elderly-discretized.csv"
datasetPath <- "bolsa-IC\\HeartDisease\\ECoL\\datasets\\elderly-discretized.csv"
dataset <- read.csv(datasetPath)

# Setting the target attribute
dataset$num <- as.factor(dataset$num)

# Calculating the complexity of the dataset and saving the results in a file
sink(file = "bolsa-IC\\HeartDisease\\ECoL\\outputs\\outputs_complex\\output-elderly-discretized.txt")
cat("Dataset Name:", datasetName, "\n")
cat("Number of Instances:", nrow(dataset), "\n")
cat("Number of Features:", ncol(dataset), "\n")
cat("Target attribute: num\n")

cat("\nComplexity Measures:\n")
complexity_result <- ECoL::complexity(num ~ ., dataset)
print(complexity_result)