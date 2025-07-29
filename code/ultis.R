# Utility functions for consistent plotting themes and settings

# Custom theme for bar plots
theme_custom_bar <- function() {
  theme_bw() +
    theme(
      legend.position = "top",
      axis.text = element_text(size = 12),
      axis.title = element_text(size = 14),
      plot.title = element_text(hjust = 0.5, size = 14),
      panel.grid.major.y = element_blank()
    )
}

# Custom theme for rotated x-axis labels
theme_custom_rotated <- function() {
  theme_bw() +
    theme(
      axis.text.x = element_text(angle = 45, hjust = 1, size = 12),
      axis.text.y = element_text(size = 12),
      axis.title = element_text(size = 14),
      plot.title = element_text(hjust = 0.5, size = 14)
    )
}