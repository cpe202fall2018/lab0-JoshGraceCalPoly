import unittest
import io, sys
from planets import *

class Test_planets(unittest.TestCase):

    # run a test to confirm the result with a normal weight
    def test_01(self):
        sys.stdin = io.StringIO("136") # Pass the weight to the input of the method
        sys.stdout = student_output = io.StringIO() # Read the print statement from the method
        expected_out = "What do you weigh on earth? \nOn Mars you would weigh 51.68 pounds.\nOn Jupiter you would weigh 318.24 pounds." # stage the expected answer
        weight_on_planets() # run weight on planets to calculate the weight on Mars/ Jupiter
        self.assertEqual(expected_out, student_output.getvalue().strip()) # check if the return value of weight_on_planets is what we expected

    # run a second test to confirm the result with a smaller value
    def test_02(self):
        sys.stdin = io.StringIO("1")
        sys.stdout = student_output = io.StringIO()        
        expected_out = "What do you weigh on earth? \nOn Mars you would weigh 0.38 pounds.\nOn Jupiter you would weigh 2.34 pounds."
        weight_on_planets()
        self.assertEqual(expected_out, student_output.getvalue().strip())

# run the main method
if __name__ == "__main__":
        unittest.main()