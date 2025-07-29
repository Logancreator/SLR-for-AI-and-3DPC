# Analyze and visualize plant type distribution
library(ggplot2)
library(tidyr)
source("scripts/utils.R")

# Calculate unique plant types per paper
data$Plant_count <- sapply(lapply(strsplit(as.character(data$`Plant type2`), "; "), unique), length)

# Summarize plant count
draw_data <- as.data.frame(table(data$Plant_count)) %>%
  rename(Number_of_Plant_Species = Var1, Count = Freq)

# Plot frequency of plant types
plant_freq <- as.data.frame(table(unlist(lapply(strsplit(as.character(data$`Plant type2`), "; "), unique)))) %>%
  rename(Plant_Type = Var1, Count = Freq) %>%
  arrange(desc(Count))

ggplot(plant_freq, aes(x = Plant_Type, y = Count)) +
  geom_col(color = "black", fill = "darkgreen", alpha = 0.6) +
  geom_text(aes(label = Count), vjust = 1.2) +
  geom_point(color = "black", size = 3) +
  theme_custom_rotated() +
  labs(title = "Frequency of Plant Types", x = "Plant Type", y = "Number of Studies")

# Save plot
ggsave("figure/Plant_species_count.pdf", width = 6, height = 5)