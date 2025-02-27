
def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Check if the BMI is above a certain limit.

    Args:
        bmi: A list of BMIs.
        limit: The limit to check against.

    Returns:
        A list of booleans.
    """
    return [bmi[i] > limit for i in range(len(bmi))]


def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """
    Calculate the BMI for a list of heights and weights.

    Args:
        height: A list of heights in meters.
        weight: A list of weights in kilograms.

    Returns:
        A list of BMIs.
    """
    return [weight[i] / height[i] ** 2 for i in range(len(height))]
