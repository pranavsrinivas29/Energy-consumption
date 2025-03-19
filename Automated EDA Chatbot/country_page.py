# 📄 country_page.py
from base_page import BaseAnalysisPage
import streamlit as st
import plotly.express as px

class CountryPage(BaseAnalysisPage):
    def __init__(self):
        super().__init__("📍 Country Wise Energy Consumption", 
                         "Country_Consumption_TWH.csv", 
                         "EDA_summary_country.csv")

    def show_analysis(self, df_data):
        """Displays an interactive Plotly chart where the user selects X & Y axes."""

        st.subheader("📊 Interactive Data Visualization")

        # Ensure 'Year' is treated as a column (not an index)
        if "Year" not in df_data.columns:
            st.error("Year column not found in the dataset!")
            return

        # Select Year Range
        min_year, max_year = int(df_data["Year"].min()), int(df_data["Year"].max())
        selected_years = st.slider("Select Year Range", min_year, max_year, (min_year, max_year))

        # Select Multiple Countries
        country_columns = [col for col in df_data.columns if col != "Year"]  # Exclude 'Year' from selection
        selected_countries = st.multiselect("Select Countries", country_columns, default=country_columns[:3]) 

        # Filter Data
        df_filtered = df_data[(df_data["Year"] >= selected_years[0]) & (df_data["Year"] <= selected_years[1])]
        
        # Melt Data for better visualization (long format)
        df_melted = df_filtered.melt(id_vars=["Year"], value_vars=selected_countries, var_name="Country", value_name="Consumption")

        # Plot
        fig = px.line(df_melted, x="Year", y="Consumption", color="Country",
                      title="Energy Consumption Over Years",
                      labels={"Consumption": "TWh", "Year": "Year"},
                      markers=True)

        st.plotly_chart(fig, use_container_width=True)

    
def show_country_page():
    page = CountryPage()
    page.show_page()