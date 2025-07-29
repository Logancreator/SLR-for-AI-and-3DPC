# Analyze and visualize algorithm categories
library(ggplot2)
source("scripts/utils.R")

# Define algorithm categories
algorithm_categories <- list(
  `Point-based Networks` = c("PointNet", "PointNet++", ...),  # Add all relevant algorithms
  `Transformer Networks` = c("Point Transformer", ...),
  # Add other categories as in your original code
)

# Process algorithms by year
algorithm_year_df <- data.frame(Algorithm = character(), Year = numeric())
for (i in 1:nrow(data)) {
  algorithms <- trimws(unlist(strsplit(data$`Algorithms (ML) (for 3dpc) proposed`[i], "; |,")))
  temp_df <- data.frame(Algorithm = algorithms, Year = data$`Year Study`[i])
  algorithm_year_df <- rbind(algorithm_year_df, temp_df)
}

# Map algorithms to categories
get_category <- function(alg) {
  for (cat in names(algorithm_categories)) {
    if (alg %in% algorithm_categories[[cat]]) return(cat)
  }
  return("Unclassified")
}
algorithm_year_df$Category <- sapply(algorithm_year_df$Algorithm, get_category)

# Summarize and plot
category_counts <- algorithm_year_df %>%
  group_by(Category, Year) %>%
  summarise(Count = n(), .groups = "drop")

ggplot(category_counts, aes(x = Year, y = Count, fill = Category)) +
  geom_col() +
  scale_fill_aaas(alpha = 0.5) +
  theme_custom_rotated() +
  labs(x = "Year", y = "Algorithm Count", fill = "Algorithm Class")

# Save plot
ggsave("figure/DL_Type.pdf", width = 8, height = 4)