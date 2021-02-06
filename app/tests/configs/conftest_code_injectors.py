import pytest


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
