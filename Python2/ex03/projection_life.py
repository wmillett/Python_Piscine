from load_csv import load
import matplotlib.pyplot as plt
import sys
import pandas as pd


def convert_value(value):
    """
    Convert values like '81k' to 81000.
    Args:
        Takes a string value.
    Returns:
        Converted value.
    """
    if isinstance(value, str):
        if value.endswith('k'):
            return float(value[:-1]) * 1_000
    return float(value)


def main(args):
    """
    Compare the population of Germany to another country.
    Args:
        args: Command line arguments (country to examine).
    Returns:
        None
    """
    if len(args) > 1:
        print("Usage: python aff_pop.py <country>")
        return
    if len(args) == 0:
        args = ["Germany"]
    try:
        df_population = load("life_expectancy_years.csv")
        if df_population is None:
            raise ValueError("Failed to load data")
        df_income = load(
            "income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
        if df_income is None:
            raise ValueError("Failed to load data")

        country = args[0]
        population_df = df_population[df_population["country"] == country]
        income_df = df_income[df_income["country"] == country]

        if population_df.empty or income_df.empty:
            raise ValueError("Missing data for {country}")

        population_df = (population_df.drop(columns=["country"]).transpose())
        population_df.index = population_df.index.astype(int)
        income_df = (income_df.drop(columns=["country"]).transpose())
        income_df.index = income_df.index.astype(int)

        merged_df = pd.merge(population_df, income_df)

        merged_df = (merged_df[(merged_df.index >= 1800) &
                (merged_df.index <= 2050)])

        plt.plot(merged_df.index, merged_df.values, label=country)

        plt.title("1900")
        plt.xlabel("Gross domestic product")
        plt.ylabel("Life Expectancy")
        plt.show()
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


if __name__ == "__main__":
    main(sys.argv[1:])
