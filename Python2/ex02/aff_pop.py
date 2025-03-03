from load_csv import load
import matplotlib.pyplot as plt
import sys


def convert_population(value):
    """
    Convert a population value to an integer.
    Args:
        value: The population value to convert.
    Returns:
        The converted population value.
    """
    if isinstance(value, str):
        if value.endswith('k'):
            return float(value[:-1]) * 1_000
        elif value.endswith('M'):
            return float(value[:-1]) * 1_000_000
    return float(value)


def main(args):
    """
    Compare the population of Germany to another country.
    Args:
        args: Command line arguments (country to compare or none).
        Returns:
        None
    """
    if len(args) > 1:
        print("Usage: python aff_pop.py <country>")
        return
    if len(args) == 0:
        args = ["Bosnia and Herzegovina"]
    try:
        df = load("population_total.csv")
        if df is None:
            raise ValueError("Failed to load data")
        germany_df = df[df["country"] == "Germany"]
        if germany_df.empty:
            raise ValueError("Missing data for Germany")
        compare_country = args[0]
        compare_df = df[df["country"] == compare_country]
        if compare_df.empty:
            raise ValueError("Missing data for {compare_country}")
        germany_df = (germany_df.drop(columns=["country"]).
                      applymap(convert_population).transpose())
        germany_df.index = germany_df.index.astype(int)
        germany_df = germany_df[(germany_df.index >= 1800) &
                                (germany_df.index <= 2050)]

        compare_df = (compare_df.drop(columns=["country"]).
                      applymap(convert_population).transpose())
        compare_df.index = compare_df.index.astype(int)
        compare_df = compare_df[(compare_df.index >= 1800) &
                                (compare_df.index <= 2050)]

        plt.plot(germany_df.index, germany_df.values, label="Germany")
        plt.plot(compare_df.index, compare_df.values, label=compare_country)

        plt.title("Population Projections")
        plt.xlabel("Year")
        plt.ylabel("Population")
        plt.yticks([20_000_000, 40_000_000, 60_000_000, 80_000_000],
                   ['20M', '40M', '60M', '80M'])
        plt.legend(loc='lower right')
        plt.show()
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


if __name__ == "__main__":
    main(sys.argv[1:])
