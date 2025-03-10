from typing import Any, List, Tuple


def calculate_mean(data: List[float]) -> float:
    return sum(data) / len(data)


def calculate_median(data: List[float]) -> float:
    sorted_data = sorted(data)
    n = len(sorted_data)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_data[mid - 1] + sorted_data[mid]) / 2
    else:
        return sorted_data[mid]


def calculate_quartiles(data: List[float]) -> Tuple[float, float]:
    sorted_data = sorted(data)
    # n = len(sorted_data)
    q1 = calculate_percentile(sorted_data, 0.25)
    q3 = calculate_percentile(sorted_data, 0.75)
    return q1, q3


def calculate_percentile(data: List[float], percentile: float) -> float:
    sorted_data = sorted(data)
    k = (len(sorted_data) - 1) * percentile
    f = int(k)
    c = k - f
    if f + 1 < len(sorted_data):
        return sorted_data[f] * (1 - c) + sorted_data[f + 1] * c
    else:
        return sorted_data[f]


def calculate_std(data: List[float]) -> float:
    mean = calculate_mean(data)
    variance = sum((x - mean) ** 2 for x in data) / len(data)
    return variance ** 0.5


def calculate_variance(data: List[float]) -> float:
    mean = calculate_mean(data)
    return sum((x - mean) ** 2 for x in data) / len(data)


def ft_statistics(*args: Any, **kwargs: Any) -> None:
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
