import subprocess


print("Test for ft_filter:\n")
# Example 1: Filter even numbers
numbers = [1, 2, 3, 4, 5, 6]
filtered = ft_filter(lambda x: x % 2 == 0, numbers)
print(list(filtered))  # Output: [2, 4, 6]

# Example 2: Filter out falsy values
values = [0, 1, False, True, "", "Hello", None]
filtered = ft_filter(None, values)
print(list(filtered))  # Output: [1, True, 'Hello']