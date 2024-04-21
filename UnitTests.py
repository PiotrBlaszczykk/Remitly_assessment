#Piotr Błaszczyk Remitly Internship 2024

import unittest
from main import verify

"""
   tests 9, 10, 11 and 12 handle exceptions and should return True
   
   the task specifies: "Method should return logical false 
   if an input JSON Resource field contains a single asterisk 
   and true in any other case"

   So I will take that literally and exceptions will return True
"""

class UnitTests(unittest.TestCase):

    def test_1(self):
        # "*" in Resource
        expected_result = False
        actual_result = verify('tests/test1.json')
        self.assertEqual(actual_result, expected_result,
                         f"Failed test1: Expected {expected_result}, got {actual_result}")

    def test_2(self):
        # "aaaaa" in Resource
        expected_result = True
        actual_result = verify('tests/test2.json')
        self.assertEqual(actual_result, expected_result,
                         f"Failed test2: Expected {expected_result}, got {actual_result}")

    def test_3(self):
        # "******" in Resource
        expected_result = True
        actual_result = verify('tests/test3.json')
        self.assertEqual(actual_result, expected_result,
                         f"Failed test3: Expected {expected_result}, got {actual_result}")

    def test_4(self):
        # empty "" in Resource
        expected_result = True
        actual_result = verify('tests/test4.json')
        self.assertEqual(actual_result, expected_result,
                         f"Failed test4: Expected {expected_result}, got {actual_result}")

    def test_5(self):
        # error signs � in Resource
        expected_result = True
        actual_result = verify('tests/test5.json')
        self.assertEqual(actual_result, expected_result,
                         f"Failed test5: Expected {expected_result}, got {actual_result}")

    def test_6(self):
        # random characters
        expected_result = True
        actual_result = verify('tests/test6.json')
        self.assertEqual(actual_result, expected_result,
                         f"Failed test6: Expected {expected_result}, got {actual_result}")

    def test_7(self):
        # long string of 1 million 'X' in Resource
        expected_result = True
        actual_result = verify('tests/test7.json')
        self.assertEqual(actual_result, expected_result,
                         f"Failed test7: Expected {expected_result}, got {actual_result}")

    def test_8(self):
        # " *" in Resources, one space before *
        expected_result = True
        actual_result = verify('tests/test8.json')
        self.assertEqual(actual_result, expected_result,
                         f"Failed test8: Expected {expected_result}, got {actual_result}")

    # tests 9, 10, 11 and 12 handle exceptions and should return False
    def test_9(self):
        # empty json file, should return False
        expected_result = True
        actual_result = verify('tests/test9.json')
        self.assertEqual(actual_result, expected_result,
                         f"Failed test9: Expected {expected_result}, got {actual_result}")


    def test_10(self):
        # total chaos in json file, should return True
        expected_result = True
        actual_result = verify('tests/test10.json')
        self.assertEqual(actual_result, expected_result,
                         f"Failed test10: Expected {expected_result}, got {actual_result}")

    def test_11(self):
        # file doesn't exist, should return True
        expected_result = True
        actual_result = verify('tests/this_file_doesnt_exist.json')
        self.assertEqual(actual_result, expected_result,
                         f"Failed test11: Expected {expected_result}, got {actual_result}")

    def test_12(self):
        # invalid input, not a file path but a random array, should return True
        expected_result = True
        actual_result = verify(["Piotr", "Blaszczyk", 2024])
        self.assertEqual(actual_result, expected_result,
                         f"Failed test12: Expected {expected_result}, got {actual_result}")

if __name__ == '__main__':
    unittest.main()
