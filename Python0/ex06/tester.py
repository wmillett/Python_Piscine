import unittest
import subprocess


class TestFilterProgram(unittest.TestCase):
    def run_program(self, function_arg, iterable_arg):
        """
        Helper function to run the ft_filter.py program with the given 
        arguments and return its output as a list.
        """
        # Run the program as a subprocess
        result = subprocess.run(
            ["python", "ft_filter.py", function_arg, iterable_arg],
            capture_output=True,
            text=True
        )
        # Check if the program ran successfully
        if result.returncode != 0:
            self.fail(f"Program failed with error: {result.stderr}")
        # Parse the output (which should be a list)
        try:
            return eval(result.stdout.strip())
        except Exception as e:
            self.fail(f"Failed to parse program output: {e}")

    def test_filter_with_lambda(self):
        # Test with a lambda function
        print("Test with a lambda function\n")
        iterable = "[1, 2, 3, 4, 5]"
        function = "lambda x: x > 2"
        result = self.run_program(function, iterable)
        self.assertEqual(result, [3, 4, 5])

    def test_filter_with_none(self):
        # Test with None as the function (filters out falsy values)
        print("Test with None as the function\n")
        iterable = "[0, 1, False, True, '', 'hello', [], [1, 2]]"
        function = "None"
        result = self.run_program(function, iterable)
        self.assertEqual(result, [1, True, "hello", [1, 2]])

    def test_filter_with_strings(self):
        # Test with strings
        print("Test with strings\n")
        iterable = "['apple', 'banana', 'cherry', 'date']"
        function = "lambda x: 'a' in x"
        result = self.run_program(function, iterable)
        self.assertEqual(result, ["apple", "banana", "date"])

    def test_filter_with_empty_iterable(self):
        # Test with an empty iterable
        print("Test with an empty iterable\n")
        iterable = "[]"
        function = "lambda x: x > 2"
        result = self.run_program(function, iterable)
        self.assertEqual(result, [])

    def test_filter_with_no_function(self):
        # Test with no function (implicitly filters out falsy values)
        print("Test with no function\n")
        iterable = "[0, 1, 2, 3, 4]"
        function = "None"
        result = self.run_program(function, iterable)
        self.assertEqual(result, [1, 2, 3, 4])

    def test_filter_with_complex_iterable(self):
        # Test with a complex iterable (list of dictionaries)
        print("Test with a complex iterable\n")
        iterable = (
            "[{'name': 'Alice', 'age': 25}, "
            "{'name': 'Bob', 'age': 17}, "
            "{'name': 'Charlie', 'age': 30}]"
        )
        function = "lambda x: x['age'] >= 18"
        result = self.run_program(function, iterable)
        self.assertEqual(result, [
            {"name": "Alice", "age": 25},
            {"name": "Charlie", "age": 30},
        ])


if __name__ == "__main__":
    unittest.main()
