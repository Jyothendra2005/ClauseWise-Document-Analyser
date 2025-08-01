from fastapi import APIRouter
from pydantic import BaseModel
from backend.core.pipeline import answer_query

router = APIRouter()

class QueryReq(BaseModel):
    question: str

@router.post("/")
def query(q: QueryReq):
    answer = answer_query([], q.question)
    return {"answer": answer}
