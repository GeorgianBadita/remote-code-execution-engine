from typing import List


from pydantic import BaseModel


class Submission(BaseModel):
    language: str
    code: str
    target_function_name: str
    param_list: List[str]
    tests: List[dict]
    maximum_exec_time: str


class SubmissionResult(BaseModel):
    submission_id: str
    hase_error: bool
    passed_all: bool
    results: List[bool]
    out_of_resources: bool
    out_of_time: bool
    exit_code: int
    raw_output: str
