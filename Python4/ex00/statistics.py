from typing import Any, List, Tuple


def calculate_mean(data: List[float]) -> float:
    """
    Calculates mean of a list.

    Args:
        A list of floats.
    Returns:
        The mean of the list in float.
    """
    return sum(data) / len(data)


def calculate_median(data: List[float]) -> float:
    """
    Calculates median of a list.

    Args:
        A list of floats.
    Returns:
        The median of the list in float.
    """
    sorted_data = sorted(data)
    n = len(sorted_data)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_data[mid - 1] + sorted_data[mid]) / 2
    else:
        return sorted_data[mid]


def calculate_quartiles(data: List[float]) -> Tuple[float, float]:
    """
    Calculates the quartiles of a list (q1 and q3).

    Args:
        A list of floats.
    Returns:
        A Tuple of the quartiles in float (q1 and q3).
    """
    sorted_data = sorted(data)
    # n = len(sorted_data)
    q1 = calculate_percentile(sorted_data, 0.25)
    q3 = calculate_percentile(sorted_data, 0.75)
    return q1, q3


def calculate_percentile(data: List[float], percentile: float) -> float:
    """
    Calculate the value at a specific percentile of a list of floats.

    Args:
        data (List[float]): A list of numerical values (floats) for which
            the percentile is to be calculated.
        percentile (float): A float between 0 and 1 representing
            the desired percentile. For example,
            0.25 represents the 25th percentile, 0.5 represents
            the median (50th percentile),
            and 1 represents the maximum value in the data.
    Returns:
        float: The value corresponding to the given percentile
        in the sorted list of data.
    """
    sorted_data = sorted(data)
    k = (len(sorted_data) - 1) * percentile
    f = int(k)
    c = k - f
    if f + 1 < len(sorted_data):
        return sorted_data[f] * (1 - c) + sorted_data[f + 1] * c
    else:
        return sorted_data[f]


def calculate_std(data: List[float]) -> float:
    """
     Calculate the standard deviation of a list of floats.

    Args:
        data (List[float]): A list of numeric values (floats) for which
        to calculate the standard deviation.

    Returns:
        float: The standard deviation of the given list of floats.

    Example:
        >>> calculate_std([1.0, 2.0, 3.0])
        0.816496580927726
    """
    mean = calculate_mean(data)
    variance = sum((x - mean) ** 2 for x in data) / len(data)
    return variance ** 0.5


def calculate_variance(data: List[float]) -> float:
    """
    Calculate the variance of a list of floats.

    Args:
        data (List[float]): A list of numeric values (floats)
        for which to calculate the variance.

    Returns:
        float: The variance of the given list of floats.

    Example:
        >>> calculate_variance([1.0, 2.0, 3.0])
        0.6666666666666666
    """
    mean = calculate_mean(data)
    return sum((x - mean) ** 2 for x in data) / len(data)


def ft_statistics(*args: Any, **kwargs: Any) -> None:
    """
    Calculate and display various statistical measures
    (mean, median, quartiles, standard deviation, variance)
    for a given list of values.

    Args:
        *args (Any): A variable-length argument list
            representing the data to calculate statistics on.
        **kwargs (dict): Keyword arguments specifying which statistics
            to calculate. Valid keys include:
                         'mean', 'median', 'quartile', 'std', 'var'.

    Returns:
        None: This function prints the results of the requested statistics.

    Raises:
        Exception: If an invalid operation is requested or
        an error occurs during calculation.

    Example:
        >>> ft_statistics(1, 2, 3, mean='mean', var='var')
        mean : 2.0
        var : 0.6666666666666666
    """
    accepted_var = ['mean', 'median',
                    'quartile', 'std', 'var']

    if not args:
        for accepted_var in kwargs:
            print("ERROR")
        return

    try:
        if 'mean' in kwargs.values():
            mean = calculate_mean(args)
            print(f"mean : {mean}")
        if 'median' in kwargs.values():
            median = calculate_median(args)
            print(f"median : {median}")
        if 'quartile' in kwargs.values():
            q1, q3 = calculate_quartiles(args)
            print(f"quartile : [{q1}, {q3}]")
        if 'std' in kwargs.values():
            std = calculate_std(args)
            print(f"std : {std}")
        if 'var' in kwargs.values():
            var = calculate_variance(args)
            print(f"var : {var}")
    except Exception as e:
        print(f"ERROR: {e}")
