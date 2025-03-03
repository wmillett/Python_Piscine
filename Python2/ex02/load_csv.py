import pandas as pd


def load(path: str) -> pd.DataFrame:
    """
    Load a dataset from a CSV file.
    Args:
        Path: The path to the CSV file.
    Returns:
        The loaded dataset.
    """
    try:
        df = pd.read_csv(path)
        print(f"Loading dataset of dimensions {df.shape}")
        return df
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
