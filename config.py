import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


# Define relative paths for datasets
DATA_PATHS = {
    "continent": os.path.join(ROOT_DIR, "data", "Continent_Consumption_TWH.csv"),
    "country": os.path.join(ROOT_DIR, "data", "Country_Consumption_TWH.csv"),
    "non_renewable": os.path.join(ROOT_DIR, "data", "nonRenewablesTotalPowerGeneration.csv"),
    "renewable": os.path.join(ROOT_DIR, "data", "renewablePowerGeneration97-17.csv"),
    "tot_power_gen": os.path.join(ROOT_DIR, "data", "renewablesTotalPowerGeneration.csv"),
    "top_20": os.path.join(ROOT_DIR, "data", "top20CountriesPowerGeneration.csv"),
}


if __name__ == '__main__':
    print(ROOT_DIR)