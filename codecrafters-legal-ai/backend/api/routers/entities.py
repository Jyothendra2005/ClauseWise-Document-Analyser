from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def entities_dummy():
    return {"entities": []}
