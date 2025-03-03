from load_csv import load
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os
import sys


def convert_value(value):
    """
    Convert values like '81k' to 81000 and '5M' to 5000000.
    Args:
        value: A string value.
    Returns:
        Converted numeric value.
    """
    if isinstance(value, str):
        if value.endswith('k'):
            return int(float(value[:-1]) * 1000)
        elif value.endswith('M'):
            return int(float(value[:-1]) * 1000000)
    return int(value)


def main(args):
    """
    Compare the life expectancy and income for all countries for the year year.
    Args:
        Year to compare GDP and life expectancy of all countries.
    Returns:
        None.
    """
    if len(args) > 1:
        print("Usage: python3 projection_life <year>")
        return
    if len(args) == 0:
        args = ["1900"]
    if not args[0].isdigit():
        print("Please insert a year between 1800 and 2050")
        return
    try:
        year = int(args[0])
        if year < 1800 or year > 2050:
            print("Please insert a year between 1800 and 2050")
            return
        year = str(year)
        df_life_expectancy = load("life_expectancy_years.csv")
        if df_life_expectancy is None:
            raise ValueError("Failed to load life expectancy data")
        fn = "income_per_person_gdppercapita_ppp_inflation_adjusted.csv"
        df_income = load(fn)
        if df_income is None:
            raise ValueError("Failed to load income data")

        df_income.iloc[:, 1:] = df_income.iloc[:, 1:].map(convert_value)

        if year not in df_life_expectancy.columns:
            raise ValueError(f"Year {year} not found in life_expectancy data.")
        if year not in df_income.columns:
            raise ValueError(f"Year {year} not found in GDP data.")

        life_expectancy_year = (df_life_expectancy[['country', year]]
                                .rename(columns={year: 'Life Expectancy'}))
        income_year = (df_income[['country', year]]
                       .rename(columns={year: 'Income'}))

        merged_df = pd.merge(life_expectancy_year, income_year, on='country')
        LE = 'Life Expectancy'
        plt.figure(figsize=(10, 6))
        plt.scatter(merged_df['Income'], merged_df[LE], alpha=0.5)

        plt.title(f"Life Expectancy vs Income ({year})")
        plt.xlabel("Gross Domestic Income per Capita")
        plt.ylabel("Life Expectancy (Years)")
        plt.yticks(np.arange(20, 101, 5))
        # plt.xticks([])

        # For debugging
        pd.set_option('display.max_rows', None)
        pd.set_option('display.max_columns', None)
        pd.set_option('display.width', None)
        with open('output.txt', 'w') as file:
            print(merged_df, file=file)

        plt.show()

        if os.path.exists("output.txt"):
            os.remove("output.txt")
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


if __name__ == "__main__":
    main(sys.argv[1:])
