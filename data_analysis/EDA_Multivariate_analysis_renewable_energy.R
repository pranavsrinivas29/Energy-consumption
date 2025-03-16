# Load necessary libraries
library(dplyr)
install.packages("tidyr")  # Install tidyr (if not installed)
library(tidyr)  # Load tidyr package
library(readr)
library(ggplot2)  # For visualization
library(GGally)   # For pair plots
library(corrplot) # For correlation heatmap
library(factoextra) # For PCA analysis

df_renewable <- read_csv("data/renewablePowerGeneration97-17.csv")


# Remove "Year" before computing correlation matrix
cor_matrix <- cor(df_renewable %>% select(-Year) %>% select_if(is.numeric), use = "complete.obs")

# Generate a correlation heatmap
corrplot(cor_matrix, method = "color", type = "lower", tl.cex = 0.7, tl.col = "black")

# Remove "Year" before generating pair plot
ggpairs(df_renewable %>% select(-Year) %>% select_if(is.numeric))


# Perform PCA on numeric columns excluding "Year"
df_pca <- prcomp(df_renewable %>% select(-Year) %>% select_if(is.numeric), scale = TRUE)

# Scree plot to visualize explained variance
fviz_eig(df_pca)

# PCA biplot
fviz_pca_biplot(df_pca, label = "var", repel = TRUE)


df_long <- df_renewable %>%
  pivot_longer(cols = -Year, names_to = "Energy_Type", values_to = "TWh")

# Print the transformed DataFrame
print(df_long)

ggplot(df_long, aes(x = Energy_Type, y = TWh, fill = Energy_Type)) +
  geom_boxplot() +
  theme_minimal() +
  theme(axis.text.x = element_text(angle = 45, hjust = 1)) +  # Rotate x-axis labels
  labs(title = "Distribution of Renewable Energy Generation",
       x = "Energy Source",
       y = "Energy Production (TWh)") +
  scale_y_continuous(labels = scales::comma)  # Format large numbers

df_numeric <- df_renewable %>% select(-Year)

# Generate a scatterplot matrix with regression lines
ggpairs(df_numeric, 
        upper = list(continuous = wrap("cor", size = 5)),   # Correlation in upper triangle
        lower = list(continuous = wrap("smooth", method = "lm", color = "blue")), # Regression in lower triangle
        diag = list(continuous = wrap("densityDiag", alpha = 0.5))) +  # Density plots on diagonal
  theme_minimal()
