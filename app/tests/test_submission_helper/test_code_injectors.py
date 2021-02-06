import pytest
from remote_coding_compilation_engine.submission_helper.code_injectors import python_submission_code_injector


def test_WHEN_PYTHIN_test_code_format_is_correct_THEN_code_injection_returns(
    two_sum_answer_py: str,
    two_sum_test_code_py: str
):
    """
    Function for testing the happy flow for code injection in python
    """

    # WHEN
    injected_code = python_submission_code_injector(two_sum_answer_py, two_sum_test_code_py)

    # THEN
    assert "TestTwoSum" in injected_code
    assert "USER CODE START" in injected_code
    assert "USER CODE END" in injected_code


def test_WHEN_PYTHIN_test_code_format_is_not_correct_THEN_code_injection_raises(
    two_sum_answer_py: str,
):
    """
    Function for testing test code which does not respect the defined test creation format
    """

    with pytest.raises(ValueError):
        # WHEN
        python_submission_code_injector(two_sum_answer_py, "")
