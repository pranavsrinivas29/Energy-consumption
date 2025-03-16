# Load necessary libraries
library(dplyr)
install.packages("tidyr")  # Install tidyr (if not installed)
library(tidyr)  # Load tidyr package
library(readr)


setwd("/Users/pranavsrinivasvenkatesh/Projects/World Energy Consumption/")
df_country <- read_csv("data/Country_Consumption_TWH.csv")
df_continent <- read_csv("data/Continent_Consumption_TWH.csv")
df_non_renewable <- read_csv("data/nonRenewablesTotalPowerGeneration.csv")
df_renewable <- read_csv("data/renewablePowerGeneration97-17.csv")
df_tot_pow <- read_csv("data/renewablesTotalPowerGeneration.csv")
df_top20_pow <- read_csv("data/top20CountriesPowerGeneration.csv")

s<-summary(df_country)
summary(df_continent)

summary(df_non_renewable)
summary(df_renewable)

summary(df_tot_pow)
summary(df_top20_pow)

# Function to compute summary statistics for numeric variables

# Define the EDA function
univariate_eda <- function(df, filename = "EDA_summary.csv", folder = "data_analysis") {
  
  # Create the folder if it does not exist
  if (!dir.exists(folder)) {
    dir.create(folder)
  }
  
  # Construct the full path
  output_file <- file.path(folder, filename)
  
  # Compute Univariate Summary Statistics
  summary_table <- df %>%
    select_if(is.numeric) %>%
    summarise(across(everything(), list(
      Mean = ~mean(.x, na.rm = TRUE),
      Median = ~median(.x, na.rm = TRUE),
      Variance = ~var(.x, na.rm = TRUE),
      Std_Dev = ~sd(.x, na.rm = TRUE),
      Min = ~min(.x, na.rm = TRUE),
      Max = ~max(.x, na.rm = TRUE),
      IQR = ~IQR(.x, na.rm = TRUE)
    ))) %>%
    pivot_longer(cols = everything(), names_to = c("Variable", "Statistic"), names_sep = "_", values_to = "Value") %>%
    pivot_wider(names_from = "Statistic", values_from = "Value")
  
  # Compute Outlier Boundaries
  outlier_table <- df %>%
    select_if(is.numeric) %>%
    summarise(across(everything(), list(
      Q1 = ~quantile(.x, 0.25, na.rm = TRUE),
      Q3 = ~quantile(.x, 0.75, na.rm = TRUE)
    ))) %>%
    mutate(across(ends_with("_Q1"), ~ . - 1.5 * (get(gsub("_Q1", "_Q3", cur_column())) - .), .names = "Lower_Bound_{.col}"),
           across(ends_with("_Q3"), ~ . + 1.5 * (. - get(gsub("_Q3", "_Q1", cur_column()))), .names = "Upper_Bound_{.col}")) %>%
    pivot_longer(cols = everything(), names_to = c("Variable", "Statistic"), names_sep = "_", values_to = "Value") %>%
    pivot_wider(names_from = "Statistic", values_from = "Value")
  
  # Merge Summary and Outlier Tables
  final_summary <- summary_table %>%
    left_join(outlier_table, by = "Variable") %>%
    mutate(across(where(is.list), ~sapply(., toString)))
  
  # Save to CSV
  write.csv(final_summary, output_file, row.names = FALSE)
  
  # Print output message
  print(paste("EDA summary saved as", output_file))
  
  # Return final summary as output
  return(final_summary)
}
eda_result <- univariate_eda(df_country, "EDA_summary_country.csv")
eda_result <- univariate_eda(df_continent, "EDA_summary_continent.csv")
eda_result <- univariate_eda(df_non_renewable, "EDA_summary_non_renewable.csv")
eda_result <- univariate_eda(df_renewable, "EDA_summary_renewable.csv")
eda_result <- univariate_eda(df_tot_pow, "EDA_summary_tot_pow.csv")
eda_result <- univariate_eda(df_top20_pow, "EDA_summary_top20_pow.csv")
