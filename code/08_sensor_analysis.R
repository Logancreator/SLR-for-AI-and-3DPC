# Analyze and visualize sensor type trends
library(ggplot2)
library(tidyr)
source("scripts/utils.R")

# Split and summarize sensor types by year
sensor_counts <- data %>%
  mutate(SensorType = strsplit(as.character(`Sensor for point cloud`), ";\\s*")) %>%
  unnest(SensorType) %>%
  group_by(`Year Study`, SensorType) %>%
  summarise(Count = n(), .groups = 'drop') %>%
  mutate(SensorType = factor(SensorType, levels = c("LiDAR", "RGB", "RGB-D", "MSI", "HSI", "Other Type")))

# Plot stacked bar chart
ggplot(sensor_counts, aes(x = `Year Study`, y = Count, fill = SensorType)) +
  geom_bar(stat = "identity") +
  theme_custom_rotated() +
  labs(x = "Year", y = "Count", fill = "Sensor Type") +
  scale_fill_aaas(alpha = 0.5)

# Save plot
ggsave("figure/Year_SensorType.pdf", width = 6, height = 4)