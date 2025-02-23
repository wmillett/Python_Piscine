import unittest
import subprocess


class TestFilterProgram(unittest.TestCase):
    def run_filterstring(self, string_arg, length_arg):
        """
        Helper function to run the filterstring.py program with the given
        arguments and return its output as a list.
        """
        result = subprocess.run(
            ["python", "filterstring.py", string_arg, length_arg],
            capture_output=True,
            text=True
        )
        if result.returncode != 0:
            self.fail(f"filterstring.py failed with error: {result.stderr}")
        try:
            return eval(result.stdout.strip())
        except Exception as e:
            self.fail(f"Failed to parse filterstring.py output: {e}")

    def run_ft_filter(self, function_arg, iterable_arg):
        """
        Helper function to run the ft_filter.py program with the given
        arguments and return its output as a list.
        """
        result = subprocess.run(
            ["python", "ft_filter.py", function_arg, iterable_arg],
            capture_output=True,
            text=True
        )
        if result.returncode != 0:
            self.fail(f"ft_filter.py failed with error: {result.stderr}")
        try:
            return eval(result.stdout.strip())
        except Exception as e:
            self.fail(f"Failed to parse ft_filter.py output: {e}")

    # Tests for filterstring.py
    def test_filterstring_basic(self):
        print("Test filterstring.py with a basic string and length\n")
        string_arg = "'Hello the World'"
        length_arg = "4"
        result = self.run_filterstring(string_arg, length_arg)
        self.assertEqual(result, ['Hello', 'World'])

    def test_filterstring_empty_string(self):
        print("Test filterstring.py with an empty string\n")
        string_arg = "''"
        length_arg = "3"
        result = self.run_filterstring(string_arg, length_arg)
        self.assertEqual(result, [])

    def test_filterstring_invalid_length(self):
        print("Test filterstring.py with invalid length argument\n")
        string_arg = "'Hello world'"
        length_arg = "abc"
        result = subprocess.run(
            ["python", "filterstring.py", string_arg, length_arg],
            capture_output=True,
            text=True
        )
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("AssertionError", result.stderr)

    # Tests for ft_filter.py
    def test_ft_filter_lambda(self):
        print("Test ft_filter.py with a lambda function\n")
        iterable = "[1, 2, 3, 4, 5]"
        function = "lambda x: x > 2"
        result = self.run_ft_filter(function, iterable)
        self.assertEqual(result, [3, 4, 5])

    def test_ft_filter_none(self):
        print("Test ft_filter.py with None as the function\n")
        iterable = "[0, 1, False, True, '', 'hello', [], [1, 2]]"
        function = "None"
        result = self.run_ft_filter(function, iterable)
        self.assertEqual(result, [1, True, "hello", [1, 2]])

    def test_ft_filter_strings(self):
        print("Test ft_filter.py with strings\n")
        iterable = "['apple', 'banana', 'cherry', 'date']"
        function = "lambda x: 'a' in x"
        result = self.run_ft_filter(function, iterable)
        self.assertEqual(result, ["apple", "banana", "date"])

    def test_ft_filter_empty_iterable(self):
        print("Test ft_filter.py with an empty iterable\n")
        iterable = "[]"
        function = "lambda x: x > 2"
        result = self.run_ft_filter(function, iterable)
        self.assertEqual(result, [])

    def test_ft_filter_no_function(self):
        print("Test ft_filter.py with no function\n")
        iterable = "[0, 1, 2, 3, 4]"
        function = "None"
        result = self.run_ft_filter(function, iterable)
        self.assertEqual(result, [1, 2, 3, 4])

    def test_ft_filter_complex_iterable(self):
        print("Test ft_filter.py with a complex iterable\n")
        iterable = (
            "[{'name': 'Alice', 'age': 25}, "
            "{'name': 'Bob', 'age': 17}, "
            "{'name': 'Charlie', 'age': 30}]"
        )
        function = "lambda x: x['age'] >= 18"
        result = self.run_ft_filter(function, iterable)
        self.assertEqual(result, [
            {"name": "Alice", "age": 25},
            {"name": "Charlie", "age": 30},
        ])


if __name__ == "__main__":
    unittest.main()
