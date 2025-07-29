# Analyze and visualize public data usage
library(ggplot2)
library(gridExtra)
source("scripts/utils.R")

# Prepare data
df <- data %>%
  mutate(Use_Public_Data = factor(`Whether to use public data`, levels = c(0, 1), labels = c("No", "Yes")))

# Pie chart
pie_data <- df %>% group_by(Use_Public_Data) %>% summarise(Count = n()) %>%
  mutate(Percentage = Count / sum(Count) * 100)
pie_plot <- ggplot(pie_data, aes(x = "", y = Percentage, fill = Use_Public_Data)) +
  geom_bar(stat = "identity", width = 1) +
  coord_polar("y") +
  geom_text(aes(label = paste0(round(Percentage, 1), "%")), position = position_stack(vjust = 0.5), color = "white") +
  scale_fill_manual(values = c("Yes" = "#66C2A5", "No" = "#8DA0CB")) +
  theme_void() +
  labs(title = "Public Data Used", fill = "Use Public Data") +
  theme(plot.title = element_text(hjust = 0.5, size = 10, face = "bold"))

# Bar chart
bar_data <- df %>% filter(Use_Public_Data == "Yes") %>% group_by(`Year Study`) %>% summarise(Count = n())
bar_plot <- ggplot(bar_data, aes(x = factor(`Year Study`), y = Count)) +
  geom_bar(stat = "identity", fill = "#66C2A5", width = 0.8) +
  theme_custom_rotated() +
  labs(title = "Yearly Distribution of Studies Using Public Data", x = "Year", y = "Number of Studies")

# Combine plots
combined_plot <- grid.arrange(pie_plot, bar_plot, ncol = 2, widths = c(1, 0.6))
ggsave(plot = combined_plot, "figure/PublicData.pdf", width = 12, height = 8)