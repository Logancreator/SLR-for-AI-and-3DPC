# Analyze and visualize DL/ML trends
library(ggplot2)
library(ggsci)
source("scripts/utils.R")

# Summarize DL/ML usage by year
counts_df <- as.data.frame(table(data$`Year Study`, data$`DL or ML for 3dpc`)) %>%
  filter(Var1 != 2025) %>%
  group_by(Var1) %>%
  mutate(Freq = Freq / sum(Freq)) %>%
  rename(Year = Var1, Class = Var2, Proportion = Freq)

# Plot stacked bar chart
ggplot(counts_df, aes(x = Year, y = Proportion * 100, fill = Class)) +
  geom_col(color = "black", size = 0.3) +
  scale_fill_npg(alpha = 0.7) +
  scale_y_continuous(labels = scales::percent_format(scale = 1), breaks = seq(0, 100, 20)) +
  theme_custom_rotated() +
  labs(x = NULL, y = "Proportion (%)", fill = "Algorithm Type", 
       title = "Trends in Algorithm Usage (2010–2024)") +
  geom_vline(xintercept = 2017, linetype = "dashed", color = "grey50")

# Save plot
ggsave("figure/Year_DL_ML_count.pdf", width = 6, height = 4, dpi = 300)