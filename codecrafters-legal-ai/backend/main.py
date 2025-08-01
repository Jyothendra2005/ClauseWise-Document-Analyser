

from fastapi import FastAPI
from backend.api.routers import upload, query, simplify, classify, entities

app = FastAPI(title="Legal Doc Intelligence")

# Add a root endpoint for testing
@app.get("/")
def read_root():
    return {"message": "Legal Doc Intelligence API is running!"}

app.include_router(upload.router, prefix="/upload", tags=["upload"])
app.include_router(query.router, prefix="/query", tags=["query"])
app.include_router(simplify.router, prefix="/simplify", tags=["simplify"])
app.include_router(classify.router, prefix="/classify", tags=["classify"])
app.include_router(entities.router, prefix="/entities", tags=["entities"])
