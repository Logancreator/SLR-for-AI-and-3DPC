# Load required libraries and data
library(readxl)
library(dplyr)

# Set working directory
setwd("E:/git/phenomics/review")

# Load main dataset
data <- read_excel("asreview/SLR Data Table6.xlsx", sheet = "SLR Papers - Jianye Chang")

# Load additional citation data
citation_data <- read.csv("asreview/Final.csv")

# Merge citation and item type data based on DOI
data <- data %>%
  mutate(Citation = citation_data$Citation[match(`DOI REFERENCE`, citation_data$DOI)],
         `Item Type` = citation_data$Item.Type[match(`DOI REFERENCE`, citation_data$DOI)])

# Save merged citation and item type data
write.csv(data %>% select(`DOI REFERENCE`, Citation, `Item Type`), 
          file = "citation_and_item_type.csv", row.names = FALSE)

# Export high-citation data (citation >= 50)
high_citation_data <- data %>% filter(Citation >= 50)
write_xlsx(high_citation_data, "high_citation_data.xlsx")