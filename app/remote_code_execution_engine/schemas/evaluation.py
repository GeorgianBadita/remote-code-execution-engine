from typing import List


from pydantic import BaseModel


class EvaluationResult(BaseModel):
    submission_id: str
    has_error: bool
    results: List[bool]
    out_of_resources: bool
    out_of_time: bool
    exit_code: int
    raw_output: str
