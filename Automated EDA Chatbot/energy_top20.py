from base_page import BaseAnalysisPage
import streamlit as st
import plotly.express as px

class EnergyTop20(BaseAnalysisPage):
    def __init__(self):
        super().__init__("🌍Top 20 Energy consumption", "top20CountriesPowerGeneration.csv", "EDA_summary_top20_pow.csv")
        
    def show_bar_chart(self, df_data):
        """Bar Chart: Top 20 Energy-Consuming Countries"""
        st.subheader("📊 Top 20 Energy Consumers")

        # Sort by Total Energy Consumption
        df_sorted = df_data.sort_values(by="Total (TWh)", ascending=False)

        # Plot
        fig = px.bar(df_sorted, x="Total (TWh)", y="Country", orientation="h",
                     title="Top 20 Energy-Consuming Countries",
                     labels={"Total (TWh)": "Energy Consumption (TWh)", "Country": "Country"},
                     color="Total (TWh)", color_continuous_scale="blues")
        st.plotly_chart(fig, use_container_width=True)

    def show_pie_chart(self, df_data):
        """Pie Chart: Breakdown of Energy Sources for Selected Country"""
        st.subheader("🍰 Energy Source Breakdown")

        selected_country = st.selectbox("Select a Country", df_data["Country"].unique())

        # Filter Data for Selected Country
        df_selected = df_data[df_data["Country"] == selected_country].drop(columns=["Country", "Total (TWh)"])
        df_melted = df_selected.melt(var_name="Energy Type", value_name="TWh")

        # Plot
        fig = px.pie(df_melted, names="Energy Type", values="TWh",
                     title=f"Energy Consumption Breakdown - {selected_country}")
        st.plotly_chart(fig, use_container_width=True)

    def show_world_map(self, df_data):
        """World Map: Energy Consumption Across Countries"""
        st.subheader("🌍 Energy Consumption - Global View")

        # Plot World Map
        fig = px.choropleth(df_data, locations="Country", locationmode="country names", color="Total (TWh)",
                             title="Global Energy Consumption",
                             color_continuous_scale="reds", labels={"Total (TWh)": "Total Energy Consumption (TWh)"})
        st.plotly_chart(fig, use_container_width=True)

    def show_page(self):
        """Displays a tab layout for switching between different analyses."""
        st.title("🌍 Top 20 Energy Consumption")

        df_data, df_stats_cleaned = self.load_data()
        if df_data is None:
            return

        # Create Tabs
        tab_overview, tab_bar, tab_pie, tab_worldmap = st.tabs(
            ["📊 Overview", "📊 Top 20 Countries", "🍰 Energy Breakdown", "🌍 World Map"]
        )

        with tab_overview:
            super().show_overview(df_data, df_stats_cleaned)

        with tab_bar:
            self.show_bar_chart(df_data)

        with tab_pie:
            self.show_pie_chart(df_data)

        with tab_worldmap:
            self.show_world_map(df_data)

def show_top20_page():
    page = EnergyTop20()
    page.show_page()