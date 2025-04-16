from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional
import scheduler as scheduler
#from scheduler import schedule_tasks

app = FastAPI()


class TaskProps(BaseModel):
    name: str
    description: Optional[str] = None
    start: Optional[str] = None
    end: Optional[str] = None
    intervalStart: Optional[str] = None
    intervalEnd: Optional[str] = None
    travelTime: Optional[int] = 0


@app.get("/")
def root():
    return {"message": "FastAPI is working!"}


@app.post("/schedule")
def schedule(tasks: List[TaskProps]):
    result = scheduler.schedule_tasks(tasks)
    return result
