# Analyze and visualize publication trends by year
library(ggplot2)
source("scripts/utils.R")

# Filter out 2025 data
data_filtered <- data %>% filter(`Year Study` != 2025)

# Prepare data for plotting
draw_data <- as.data.frame(table(data_filtered$`Year Study`))
colnames(draw_data) <- c("Year", "Frequency")

# Define color palette
mako_palette <- c("#0B0405", "#120E35", "#1B194B", "#1B2A5F", "#13306F", "#1B4B6F", 
                  "#2A6773", "#4A8573", "#7BA36F", "#B7C16B", "#D9D56A", "#EDE06A", 
                  "#F6E161", "#FDE64E")

# Plot combined bar and line chart
ggplot(draw_data, aes(x = Year, y = Frequency)) +
  geom_col(fill = "#7BA36F") +
  geom_line(aes(group = 1), color = "black") +
  geom_text(aes(label = Frequency), vjust = -0.5, color = "black") +
  geom_point(color = "black", size = 4) +
  theme_custom_rotated() +
  labs(x = NULL, y = "Number of Publications") +
  guides(fill = "none")

# Save plot
ggsave("figure/Year_Study.pdf", width = 8, height = 6)