# 📄 eda_analysis.py
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Ensure the reports directory exists
if not os.path.exists("eda_reports"):
    os.makedirs("eda_reports")

def automated_eda(df):
    
    # Summary Statistics
    summary = df.drop(columns=['Bound'])
    
    return summary

if __name__=="__main__":
    # Get the BASE_DIR of the current script (inside Automated EDA Chatbot/)
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    # Define the path to the folders (same level as Automated EDA Chatbot/)
    DATA_FOLDER = os.path.join(BASE_DIR, "..", "data")
    DATA_ANALYSIS_FOLDER = os.path.join(BASE_DIR, "..", "data_analysis")
    
    df = pd.read_csv(os.path.join(DATA_ANALYSIS_FOLDER, "EDA_summary_country.csv"))
    
    report = automated_eda(df)
    print(report)
    