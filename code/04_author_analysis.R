# Analyze and visualize author count distribution
library(ggplot2)
source("scripts/utils.R")

# Calculate author count per paper
data$Author_count <- sapply(strsplit(as.character(data$Author), ";"), length)

# Plot histogram with density overlay
ggplot(data, aes(x = Author_count)) +
  geom_histogram(aes(y = ..density..), fill = "#9BCD9B", color = "black", binwidth = 1, alpha = 0.7) +
  geom_density(alpha = 0.5, fill = "#FFE4B5", color = "black", adjust = 1.5) +
  theme_custom_bar() +
  labs(x = "Number of Authors per Paper", y = "Density", title = "Distribution of Author Counts") +
  scale_x_continuous(breaks = seq(min(data$Author_count), max(data$Author_count), by = 1))

# Save plot
ggsave("figure/Author_count.pdf", width = 5, height = 4)