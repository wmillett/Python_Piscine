from load_csv import load
import matplotlib.pyplot as plt
import pandas as pd


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
            return float(value[:-1]) * 1_000
        elif value.endswith('M'):
            return float(value[:-1]) * 1_000_000
    return float(value)


def main():
    """
    Compare the life expectancy and income for all countries for the year 1900.
    Args:
        None.
    Returns:
        None.
    """
    try:

        df_life_expectancy = load("life_expectancy_years.csv")
        if df_life_expectancy is None:
            raise ValueError("Failed to load life expectancy data")
        fn = "income_per_person_gdppercapita_ppp_inflation_adjusted.csv"
        df_income = load(fn)
        if df_income is None:
            raise ValueError("Failed to load income data")

        df_income.iloc[:, 1:] = df_income.iloc[:, 1:].map(convert_value)

        life_expectancy_1900 = (df_life_expectancy[['country', '1900']]
                                .rename(columns={'1900': 'Life Expectancy'}))
        income_1900 = (df_income[['country', '1900']]
                       .rename(columns={'1900': 'Income'}))

        merged_df = pd.merge(life_expectancy_1900, income_1900, on='country')

        Gdp = 'Income'

        plt.figure(figsize=(10, 6))
        plt.scatter(merged_df[Gdp], merged_df['Life Expectancy'], alpha=0.5)

        plt.title("1900")
        plt.xlabel("Gross domestic income")
        plt.ylabel("Life Expectancy (Years)")
        plt.show()
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


if __name__ == "__main__":
    main()
