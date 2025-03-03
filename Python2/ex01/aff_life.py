from load_csv import load
import matplotlib.pyplot as plt


def main():
    """
    Load life expectancy data for Germany and plot it.
    Args:
        None
    Returns:
        None
    """
    try:
        df = load("life_expectancy_years.csv")
        if df is None:
            raise ValueError("Failed to load data")
        germany_df = df[df["country"] == "Germany"]
        if germany_df.empty:
            raise ValueError("Missing data for Germany")
        germany_df = germany_df.drop(columns=["country"]).transpose()
        germany_df.index = germany_df.index.astype(int)
        plt.plot(germany_df.index, germany_df.values, label="Germany")
        plt.title("Germany Life Expectancy Projections")
        plt.xlabel("Year")
        plt.ylabel("Life Expectancy")
        plt.show()
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


if __name__ == "__main__":
    main()
