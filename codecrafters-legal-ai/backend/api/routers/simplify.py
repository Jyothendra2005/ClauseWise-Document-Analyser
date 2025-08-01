from fastapi import APIRouter
from pydantic import BaseModel
from backend.core.clause_breakdown import split_into_clauses
from backend.core.simplifier import simplify_clause

router = APIRouter()

class SimplifyRequest(BaseModel):
    text: str

@router.post("/")
def simplify(req: SimplifyRequest):
    clauses = split_into_clauses(req.text)
    simplified = [simplify_clause(c) for c in clauses]
    return {"simplified_clauses": simplified}
