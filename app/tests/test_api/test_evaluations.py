from remote_code_execution_engine import schemas

from fastapi.testclient import TestClient


def test_WHEN_submission_works_THEN_return(client: TestClient,
                                           execution: schemas.Execution,
                                           mocker,
                                           mock_send_task_no_error_submission: callable):
    """
    Function for testing the submission post call when the call is done correctly
    """

    mocker.patch(
        'remote_code_execution_engine.api.api_v1.endpoints.evaluations.celery_client.send_task',
        mock_send_task_no_error_submission
    )
    res = client.post('/api/v1/evaluations/', json=execution)

    assert res.status_code == 200


def test_WHEN_submission_fails_THEN_raise(client: TestClient,
                                          execution: schemas.Execution,
                                          mocker,
                                          mock_send_task_raise: callable):
    """
    Function for testing the submission post call when the celery worker cannot process the execution
    """

    mocker.patch(
        'remote_code_execution_engine.api.api_v1.endpoints.evaluations.celery_client.send_task',
        mock_send_task_raise
    )

    res = client.post('/api/v1/evaluations/', json=execution)

    assert res.status_code == 500
    assert "could not process the code execution" in res.text


def test_WHEN_test_code_is_not_properly_formatted_THEN_raise(client: TestClient,
                                                             execution: schemas.Execution,
                                                             mocker,
                                                             mock_send_task_no_error: callable):
    """
    Function for testing the submission post call when the test code is not properly formatted
    """

    mocker.patch(
        'remote_code_execution_engine.api.api_v1.endpoints.evaluations.celery_client.send_task',
        mock_send_task_no_error
    )

    res = client.post('/api/v1/evaluations/', json=execution)

    assert res.status_code == 400
