from remote_code_execution_engine import schemas

from fastapi.testclient import TestClient


def test_WHEN_execution_working_THEN_return(client: TestClient,
                                            execution: schemas.Execution,
                                            mocker,
                                            mock_send_task_no_error: callable):
    """
    Function for testing the execution post call when the call is done correctly
    """

    mocker.patch(
        'remote_code_execution_engine.api.api_v1.endpoints.executions.celery_client.send_task',
        mock_send_task_no_error
    )
    res = client.post('/api/v1/executions/', json=execution)

    assert res.status_code == 200
    assert "Hello World" in res.text


def test_WHEN_execution_fails_THEN_raise(client: TestClient,
                                         execution: schemas.Execution,
                                         mocker,
                                         mock_send_task_raise: callable):
    """
    Function for testing the execution post call when the celery worker cannot process the execution
    """

    mocker.patch(
        'remote_code_execution_engine.api.api_v1.endpoints.executions.celery_client.send_task',
        mock_send_task_raise
    )
    res = client.post('/api/v1/executions/', json=execution)

    assert res.status_code == 500
    assert "could not process the code execution" in res.text
