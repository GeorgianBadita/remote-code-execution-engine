import pytest

from submission_helper.submission_helper import SubmissionHelper


def test_WHEN_test_code_format_is_corrent_THEN_compose_submission_code_returns(
    two_sum_answer_py: str,
    two_sum_test_code_py: str
):
    """
    Function for testing happy flow for submission composition
    """

    final_code = SubmissionHelper.compose_submission_code(two_sum_answer_py, two_sum_test_code_py, 'python')
    assert "TestTwoSum" in final_code
    assert "USER CODE START" in final_code
    assert "USER CODE END" in final_code


def test_WHEN_test_code_format_is_incorrect_THEN_compose_submission_code_raise(
    two_sum_answer_py: str,
    two_sum_test_code_py: str
):
    """
    Function which tests that compose submission code raises when language is not supported
    """

    with pytest.raises(KeyError):
        SubmissionHelper.compose_submission_code(two_sum_answer_py, two_sum_test_code_py, 'lang')
