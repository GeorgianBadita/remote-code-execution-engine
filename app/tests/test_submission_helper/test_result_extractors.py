import pytest

from remote_coding_compilation_engine.submission_helper.result_extractors import python_result_extractor


def test_WHEN_all_py_tests_passed_THEN_result_extractor_returns_all_true(
    passed_submission_py: str
):
    """
    Function which verifies that the result extractor, returns all tests as passed
    when execution output returns true for all tests
    """

    # WHEN
    tests_execution = python_result_extractor(passed_submission_py)

    # THEN
    assert all(tests_execution)


def test_WHEN_not_all_py_tests_passed_THEN_result_extractor_returns_true_for_passed_tests_and_false_for_failed_tests(
    not_passed_submission_py: str
):
    """
    Function which verifies that the result extractor, returns mix of passed/failed tests
    when execution output returns mixed results
    """

    # WHEN
    tests_execution = python_result_extractor(not_passed_submission_py)

    # THEN
    assert tests_execution[0] is True  # First test passed
    assert tests_execution[1] is False  # Second test failed


def test_WHEN_raw_test_output_is_not_properly_formated_THEN_result_extractor_throws(
    incorrect_test_submission_output_py: str
):
    """
    Function which checks that the result extractor throws error when raw test outout
    is not properly formated
    """

    with pytest.raises(ValueError):
        python_result_extractor(incorrect_test_submission_output_py)
