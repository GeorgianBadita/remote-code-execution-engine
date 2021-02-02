import os
import pytest


@pytest.fixture
def create_hello_world_py() -> str:
    """
    Fixture which returns a simple hello world code in python
    """

    return "print('Hello World')"


@pytest.fixture
def create_infinite_loop_py() -> str:
    """
    Fixture which returns a simple inifnite loop program in python
    """

    return "while True:\n pass"


@pytest.fixture
def create_invalid_syntax_code() -> str:
    """
    Fixture which returns an inalid pytho program
    """

    return "Invalid program"


@pytest.fixture
def create_hello_world_cpp() -> str:
    """
    Fixture which returns a simple cpp hello world code
    """

    return '#include<iostream>\n using namespace std; int main() {cout << "Hello World"; return 0;}'


@pytest.fixture
def create_infinite_loop_cpp() -> str:
    """
    Fixture which returns a simple infnite loop program in cpp
    """
    return '#include<iostream>\n using namespace std; int main() {while(1){} return 0;}'


@pytest.fixture
def count_files() -> callable:
    """
    Fixture which returns a helper function for counting the number of files in a given directory

    @return: func - to be used in tests for counting number of files in a given directory

    """

    def count_files_in_dir(path: str) -> int:
        file_entries = [entry for entry in os.scandir(path) if entry.is_file()]

        return len(file_entries)

    return count_files_in_dir


@pytest.fixture
def two_sum_answer_py() -> str:
    """
    Fixture which returns the twoSum solution for python
    """

    return """
def two_sum(nums: list, target_sum: int) -> list:

    # if there are not at least two numbers
    if len(nums) < 2:
        return []

    seen_sums = set()

    for elem in nums:
        if target_sum - elem in seen_sums:
            return [elem, target_sum - elem]
        seen_sums.add(elem)
    return []
    """


@pytest.fixture
def two_sum_test_code_py() -> str:
    """
    Fixture which returns the two sum test code for python
    """

    return """

import unittest


class TestTwoSum(unittest.TestCase):

    def testTwoSum_1(self):
        array = [3, 5, -4, 8, 11, 1, -1, 6]
        targetSum = 10

        result = two_sum(array, targetSum)

        assert sum(result) == targetSum

    def testTwoSum_2(self):
        array = [4, 6, 1, -3]
        targetSum = 3

        result = two_sum(array, targetSum)

        assert sum(result) == targetSum


if __name__ == '__main__':
    unittest.main()  # run all tests
    """
