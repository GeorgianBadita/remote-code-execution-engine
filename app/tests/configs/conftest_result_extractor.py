import pytest


@pytest.fixture
def passed_submission_py() -> str:
    """
    Function which returns a passed execution output in python
    """

    return """
    ..
----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
"""


@pytest.fixture
def not_passed_submission_py() -> str:
    return """
    .F
======================================================================
FAIL: testTwoSum_1 (__main__.TestTwoSum)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/geo/Programming/remote-coding-platform-problems/TwoSum/twoSumTests.py", line 30, in testTwoSum_1
    self.assertEqual(sum(result), targetSum)
AssertionError: 11 != 10
----------------------------------------------------------------------
Ran 2 tests in 0.000s

FAILED (failures=1)
"""


@pytest.fixture
def incorrect_test_submission_output_py() -> str:
    return "incorrect test output"""
