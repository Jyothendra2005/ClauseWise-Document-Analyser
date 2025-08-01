from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def classify_dummy():
    return {"document_type": "unknown"}
