# 📄 renewable_page.py
import streamlit as st
import plotly.express as px
from base_page import BaseAnalysisPage

class RenewableEnergy(BaseAnalysisPage):
    def __init__(self):
        super().__init__("♻️ Renewable Energies", 
                         "renewablePowerGeneration97-17.csv", 
                         "EDA_summary_renewable.csv")

    def show_analysis(self, df_data):
        """Displays interactive plots for Renewable Energy trends."""
        st.subheader("📈 Renewable Energy Generation")

        # Ensure 'Year' column exists
        if "Year" not in df_data.columns:
            st.error("Year column not found in the dataset!")
            return
        
        # Select Up to 3 Years
        available_years = df_data["Year"].unique().tolist()
        selected_years = st.multiselect(
            "Select Up to 3 Years", available_years, default=available_years[:3], max_selections=3
        )

        # Select Up to 2 Energy Types
        energy_columns = [col for col in df_data.columns if col != "Year"]  # Exclude 'Year'
        selected_energies = st.multiselect(
            "Select Up to 2 Energy Types", energy_columns, default=energy_columns[:2], max_selections=2
        )

        # Validate selection
        if len(selected_years) == 0 or len(selected_energies) == 0:
            st.warning("Please select at least one year and one energy type to generate the plot.")
            return

        # Filter Data
        df_filtered = df_data[df_data["Year"].isin(selected_years)]

        # Melt Data for better visualization
        df_melted = df_filtered.melt(id_vars=["Year"], value_vars=selected_energies, var_name="Energy Type", value_name="TWh")

        # Convert Year to Category for better visualization
        df_melted["Year"] = df_melted["Year"].astype(str)

        # Plot
        fig = px.bar(df_melted, x="Year", y="TWh", color="Energy Type",
                     title="Renewable Energy Generation Over Selected Years",
                     labels={"TWh": "Energy Generated (TWh)", "Year": "Year"},
                     barmode="group")  # Group bars by year

        st.plotly_chart(fig, use_container_width=True)

def show_renewable_page():
    page = RenewableEnergy()
    page.show_page()
