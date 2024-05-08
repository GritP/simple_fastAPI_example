from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


class Data(BaseModel):
    feature_1: float
    feature_2: str

app = FastAPI(
    title="Exercise API",
    description="An API that demonstrates checking the values of inputs.",
    version="1.0.0",
)

@app.post("/data/")
async def ingest_data(data: Data):
    if data.feature_1 < 0:
        raise HTTPException(status_code=400, detail="feature_1 has to be non-negative.")
    
    if len(data.feature_2) > 280:
        raise HTTPException(status_code=400, detail="feature_2 can be at maximum 280 characters long.")
    
    return data