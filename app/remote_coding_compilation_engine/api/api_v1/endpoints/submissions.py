from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def create_submission():
    return {"message": "Hello, submission"}
