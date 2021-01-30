from typing import Optional
from pydantic import BaseModel


class Execution(BaseModel):
    language: str
    code: str
    timeout: Optional[float]


class ExecutionResult(BaseModel):
    has_error: bool
    out_of_resources: bool
    exit_code: int
    out_of_time: bool
    raw_output: str
