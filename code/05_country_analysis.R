# Analyze and visualize country count and first author country distribution
library(ggplot2)
source("scripts/utils.R")

# Calculate country count per paper
data$Country_count <- sapply(strsplit(as.character(data$Country), "; "), length)

# Plot histogram of country count
ggplot(data, aes(x = Country_count)) +
  geom_histogram(fill = "#4A8573", color = "black", binwidth = 0.5) +
  theme_custom_bar() +
  labs(x = "Number of Countries per Paper", y = "Count")

# Save plot
ggsave("figure/Country_count.pdf", width = 4, height = 4)

# Extract first country and summarize
first_countries <- sapply(strsplit(as.character(data$Country), "; "), `[`, 1)
country_counts_df <- as.data.frame(table(first_countries)) %>%
  rename(Country = first_countries, Count = Freq) %>%
  mutate(Country = case_when(
    Country %in% c("United States of America", "USA") ~ "USA",
    Country %in% c("United Kingdom", "UK") ~ "UK",
    TRUE ~ Country
  )) %>%
  group_by(Country) %>%
  summarise(Count = sum(Count)) %>%
  arrange(desc(Count))

# Plot bar chart of first author countries
ggplot(country_counts_df, aes(x = reorder(Country, Count), y = Count)) +
  geom_bar(stat = "identity", fill = "#4A8573") +
  coord_flip() +
  theme_custom_bar() +
  labs(title = "Frequency of First Author Countries", x = "Country", y = "Count")

# Save plot
ggsave("figure/first_Country_count.pdf", width = 6, height = 6)