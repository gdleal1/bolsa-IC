# R script for downloading necessary packages and calculating the complexity of a dataset using the column Sex as the sensitive attribute

# Installing and loading the ECoL package
if(!require("devtools")) {
  install.packages("devtools")
}
devtools::install_github("lpfgarcia/ECoL")
library("ECoL")


# Reading dataset
datasetName <- "intersectional-bias-reduced.csv"
datasetPath <- paste0("datasets/", datasetName)
dataset <- read.csv(datasetPath)
n_males <- sum(dataset$Sex == 'Male')
n_females <- sum(dataset$Sex == 'Female')


# Tranform the non-numeric columns to numeric
dataset$Race <- as.numeric(as.factor(dataset$Race))
dataset$Housing <- as.numeric(as.factor(dataset$Housing))
dataset$Delay <- as.numeric(as.factor(dataset$Delay))

# Using the column Sex as the sensitive attribute
dataset$Sex <- as.factor(dataset$Sex)

# Calculating the complexity of the dataset and saving the results in a file
sink(file = "output.txt")
cat("Dataset Name:", datasetName, "\n")
cat("Number of Instances:", nrow(dataset), "\n")
cat("Number of Features:", ncol(dataset), "\n")
cat("Sensitive Attribute: Sex\n")
cat("Number of males:", n_males, "\n")
cat("Number of females:", n_females, "\n")

cat("\nComplexity Measures:\n")
complexity_result <- ECoL::complexity(Sex ~ ., dataset)
print(complexity_result)











