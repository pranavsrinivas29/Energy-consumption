# 📄 continent_page.py
from base_page import BaseAnalysisPage
import streamlit as st
import plotly.express as px

class ContinentPage(BaseAnalysisPage):
    def __init__(self):
        super().__init__("🌍 Continent Wise Energy Consumption", 
                         "Continent_Consumption_TWH.csv", 
                         "EDA_summary_continent.csv")

    def show_interactive_plot(self, df_data):
        st.subheader("📊 Interactive Data Visualization")

        # Ensure 'Year' is treated as a column (not an index)
        if "Year" not in df_data.columns:
            st.error("Year column not found in the dataset!")
            return
        
        min_year, max_year = int(df_data['Year'].min()), int(df_data['Year'].max())
        selected_years = st.slider("Select Year Range", min_year, max_year, (min_year, max_year))
        
        # Select Multiple Countries
        continent_columns = [col for col in df_data.columns if col != "Year"]  # Exclude 'Year' from selection
        selected_continents = st.multiselect("Select Countries", continent_columns, default=continent_columns[:3]) 
        
        # Filter Data
        df_filtered = df_data[(df_data["Year"] >= selected_years[0]) & (df_data["Year"] <= selected_years[1])]
        
        # Melt Data for better visualization (long format)
        df_melted = df_filtered.melt(id_vars=["Year"], value_vars=selected_continents, var_name="Continent", value_name="Consumption")
        
        # Plot
        fig = px.line(df_melted, x="Year", y="Consumption", color="Continent",
                      title="Energy Consumption Over Years",
                      labels={"Consumption": "TWh", "Year": "Year"},
                      markers=True)

        st.plotly_chart(fig, use_container_width=True)
    def show_page(self):
        """Displays the analysis page with an interactive plot."""
        super().show_page()  # Display the base EDA summary

        df_data, _ = self.load_data()
        if df_data is not None:
            self.show_interactive_plot(df_data)  # Show interactive plot
            
def show_continent_page():
    page = ContinentPage()
    page.show_page()
