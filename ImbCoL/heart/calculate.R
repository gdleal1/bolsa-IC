# Creates an output.txt file with the file name, number of rows, number of rows with target 0 and number of rows with target 1

if (!require("devtools")) {
  install.packages("devtools")
}
devtools::install_github("victorhb/ImbCoL")
library("ImbCoL")

# reading datasets
filePath <- "datasets/female.csv"
dataset <- read.csv(filePath)
fileName <- basename(filePath)
numRows <- nrow(dataset)
num0 <- sum(dataset$target == 0) # Number of rows in which the target column is 0
num1 <- sum(dataset$target == 1) # Number of rows in which the target column is 1

sink(file = "output.txt")
print(fileName)
print(numRows)
print(num0)
print(num1)
ImbCoL::complexity(target ~ ., dataset)
sink(file = NULL)
