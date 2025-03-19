from base_page import BaseAnalysisPage
import streamlit as st
import plotly.express as px
from ai_summary import generate_nlp_summary

class EnergyTop20(BaseAnalysisPage):
    def __init__(self):
        super().__init__("🌍 Top 20 Energy Consumption", 
                         "top20CountriesPowerGeneration.csv", 
                         "EDA_summary_top20_pow.csv")

    def show_bar_chart(self, df_data):
        """Bar Chart: Top 20 Energy-Consuming Countries"""
        st.subheader("📊 Top 20 Energy Consumers")

        df_sorted = df_data.sort_values(by="Total (TWh)", ascending=False)

        fig = px.bar(df_sorted, x="Total (TWh)", y="Country", orientation="h",
                     title="Top 20 Energy-Consuming Countries",
                     labels={"Total (TWh)": "Energy Consumption (TWh)", "Country": "Country"},
                     color="Total (TWh)", color_continuous_scale="blues")
        st.plotly_chart(fig, use_container_width=True)

        if st.button("Summarize Top 20 Energy Trends"):
            self.summarize_bar_chart(df_sorted)

    def show_pie_chart(self, df_data):
        """Pie Chart: Breakdown of Energy Sources for Selected Country"""
        st.subheader("🍰 Energy Source Breakdown")

        selected_country = st.selectbox("Select a Country", df_data["Country"].unique())

        df_selected = df_data[df_data["Country"] == selected_country].drop(columns=["Country", "Total (TWh)"])
        df_melted = df_selected.melt(var_name="Energy Type", value_name="TWh")

        fig = px.pie(df_melted, names="Energy Type", values="TWh",
                     title=f"Energy Consumption Breakdown - {selected_country}")
        st.plotly_chart(fig, use_container_width=True)

        if st.button("Summarize Country Insights"):
            self.summarize_pie_chart(selected_country, df_melted)

    def show_world_map(self, df_data):
        """World Map: Energy Consumption Across Countries"""
        st.subheader("🌍 Energy Consumption - Global View")

        fig = px.choropleth(df_data, locations="Country", locationmode="country names", color="Total (TWh)",
                             title="Global Energy Consumption",
                             color_continuous_scale="reds", labels={"Total (TWh)": "Total Energy Consumption (TWh)"})
        st.plotly_chart(fig, use_container_width=True)

        if st.button("Summarize Global Energy Trends"):
            self.summarize_world_map(df_data)

    def summarize_bar_chart(self, df_sorted):
        """Summarizes the top and least consuming countries in the bar chart."""
        st.subheader("📄 AI-Generated Summary")

        top_country = df_sorted.iloc[-1]  # Highest energy consumption
        least_country = df_sorted.iloc[0]  # Lowest energy consumption

        summary_text = (
            f"In the **Top 20 Energy Consumers**, the highest energy consumption is observed in **{top_country['Country']}**, "
            f"which consumes **{top_country['Total (TWh)']} TWh**. "
            f"On the other hand, **{least_country['Country']}** has the lowest energy usage among the top 20, with just "
            f"**{least_country['Total (TWh)']} TWh**. This variation highlights the stark differences in energy demand "
            f"based on industrialization, economic scale, and energy policies across these nations."
        )

        ai_summary = generate_nlp_summary(summary_text)
        st.markdown(f"💡 **{ai_summary}**")

    def summarize_pie_chart(self, selected_country, df_melted):
        """Summarizes the energy breakdown in the pie chart (UNCHANGED)."""
        st.subheader("📄 AI-Generated Summary")

        top_source = df_melted.nlargest(1, "TWh")["Energy Type"].values[0]
        top_value = df_melted.nlargest(1, "TWh")["TWh"].values[0]
        least_source = df_melted.nsmallest(1, "TWh")["Energy Type"].values[0]
        least_value = df_melted.nsmallest(1, "TWh")["TWh"].values[0]

        total_energy = df_melted["TWh"].sum()
        top_share = round((top_value / total_energy) * 100, 2)
        least_share = round((least_value / total_energy) * 100, 2)

        summary_text = (
            f"In **{selected_country}**, the leading energy source is **{top_source}**, "
            f"which accounts for **{top_value} TWh**, contributing to **{top_share}%** of total energy consumption. "
            f"On the other hand, **{least_source}** remains the least utilized, generating only **{least_value} TWh** "
            f"({least_share}% of total consumption). This highlights the nation's reliance on **{top_source}**, "
            f"while **{least_source}** plays a minor role in the overall energy mix. "
            f"The distribution reflects the country's energy priorities and areas for potential diversification."
        )

        ai_summary = generate_nlp_summary(summary_text)
        st.markdown(f"💡 **{ai_summary}**")

    def summarize_world_map(self, df_data):
        """Summarizes global energy trends using the world map data."""
        st.subheader("📄 AI-Generated Summary")

        top_country = df_data.loc[df_data["Total (TWh)"].idxmax()]  # Get highest energy-consuming country

        summary_text = (
            f"🌍 **Global Energy Consumption Trends:** The country with the highest energy consumption is "
            f"**{top_country['Country']}**, using **{top_country['Total (TWh)']} TWh**. "
            f"This significant consumption underscores its industrial and economic energy demands. The global "
            f"distribution reflects how energy usage is concentrated in highly industrialized nations, while "
            f"developing regions have different energy utilization patterns."
        )

        ai_summary = generate_nlp_summary(summary_text)
        st.markdown(f"💡 **{ai_summary}**")

    def show_page(self):
        """Displays a tab layout for switching between different analyses."""
        st.title("🌍 Top 20 Energy Consumption")

        df_data, df_stats_cleaned = self.load_data()
        if df_data is None:
            return

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
