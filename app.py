from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import time, json
from logic import largest_rectangle
from database import engine, SessionLocal
from models import Base, RequestLog
Base.metadata.create_all(bind=engine)
app = FastAPI()
class MatrixInput(BaseModel):
    matrix: List[List[int]]
@app.post("/largest-rectangle")
def find_largest_rectangle(data: MatrixInput):
    start = time.time()
    number, area = largest_rectangle(data.matrix)
    turnaround = time.time() - start
    db = SessionLocal()
    log = RequestLog(
        matrix=json.dumps(data.matrix),
        result=f"Number={number}, Area={area}",
        response_time=turnaround
    )
    db.add(log)
    db.commit()
    db.close()
    return {
        "number": number,
        "area": area,
        "turnaround_time": turnaround
    }
