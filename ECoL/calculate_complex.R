# R script for downloading necessary packages and calculating the complexity of datasets 

# Installing and loading the ECoL package
if(!require("devtools")) {
  install.packages("devtools")
}
devtools::install_github("lpfgarcia/ECoL")
library("ECoL")

# Reading dataset
datasetName <- "hispanic-reduced.csv"
datasetPath <- paste0("datasets/", datasetName)
dataset <- read.csv(datasetPath)

# Tranform the non-numeric columns to numeric
dataset$Sex <- as.numeric(as.factor(dataset$Sex))
dataset$Housing <- as.numeric(as.factor(dataset$Housing))
dataset$Delay <- as.numeric(as.factor(dataset$Delay))


# Setting the target attribute
dataset$Diagnosis <- as.factor(dataset$Diagnosis)

# Calculating the complexity of the dataset and saving the results in a file
sink(file = "outputs/output-hispanic-dataset.txt")
cat("Dataset Name:", datasetName, "\n")
cat("Number of Instances:", nrow(dataset), "\n")
cat("Number of Features:", ncol(dataset), "\n")
cat("Target attribute: Diagnosis\n")

cat("\nComplexity Measures:\n")
complexity_result <- ECoL::complexity(Diagnosis ~ ., dataset)
print(complexity_result)