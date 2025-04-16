from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional
import json
from .scheduler import plan_schedule  # Importing the scheduling logic
    
app = FastAPI()

class TaskProps(BaseModel):
    id: Optional[str]
    taskName: Optional[str]
    contactName: Optional[str]
    taskDescription: Optional[str]
    placeName: Optional[str]
    itemsName: Optional[List[str]]
    startTime: Optional[int]  # Use int for time (e.g., 990 for 9:90)
    endTime: Optional[int]
    takesTime: Optional[int]
    intervalStartTime: Optional[int]
    intervalEndTime: Optional[int]
    travelTime: Optional[int]
    googleTask: Optional[bool]
    taken: Optional[bool]

# Define your endpoint to get planned schedule
@app.post("/schedule")
async def create_schedule(tasks: List[TaskProps]):
    # Call OR-Tools function to create the schedule
    planned_schedule = plan_schedule(tasks)
    return json.dumps(planned_schedule)


@app.get("/")
def root():
    return {"message": "FastAPI is working!"}
