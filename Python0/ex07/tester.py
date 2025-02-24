import subprocess
import unittest


class TestSOSProgram(unittest.TestCase):
    def run_test(self, program, args, expect_error=False):
        """
        Helper function to run the given program with the specified arguments
        and return its output as a list.

        Args:
            program (str): The program to run (e.g., "sos.py").
            args (list): The arguments to pass to the program.
            expect_error (bool): Whether to expect an error from the program.

        Returns:
            str: The program's stdout output if no error is expected.
            str: The program's stderr output if an error is expected.
        """
        result = subprocess.run(
            ["python", program] + args,
            capture_output=True,
            text=True
        )
        if expect_error:
            # If an error is expected, return the stderr output
            return result.stderr.strip()
        else:
            # If no error is expected, return the stdout output
            if result.returncode != 0:
                self.fail(f"{program} failed with error: {result.stderr}")
            return result.stdout.strip()

    def test_invalid_input(self):
        print("Test sos.py with invalid input\n")
        args = ["'Hello@World'"]
        result = self.run_test("sos.py", args, expect_error=True)
        print(f"Result: {result}\n")
        self.assertIn("Error: Invalid input", result)

    def test_no_arguments(self):
        print("Test sos.py with no arguments\n")
        args = []
        result = self.run_test("sos.py", args, expect_error=True)
        print(f"Result: {result}\n")
        self.assertIn("Error: Usage: sos.py <text>", result)

    def test_basic_input(self):
        print("Test sos.py with basic input\n")
        args = ["Hello World"]
        result = self.run_test("sos.py", args)
        print(f"Result: {result}\n")
        self.assertEqual(result, ".... . .-.. .-.. --- / .-- --- .-. .-.. -..")

    def test_numbers_input(self):
        print("Test sos.py with numbers input\n")
        args = ["12345"]
        result = self.run_test("sos.py", args)
        print(f"Result: {result}\n")
        self.assertEqual(result, ".---- ..--- ...-- ....- .....")


if __name__ == "__main__":
    unittest.main()
