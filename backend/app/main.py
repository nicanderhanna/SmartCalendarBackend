from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional
#import scheduler as scheduler
from .import scheduler

app = FastAPI()
    
class TaskProps(BaseModel):
  id: Optional[str] = None #this will be assigned by firebase

  taskName: Optional[str] = None
  contactName: Optional[str] = None
  taskDescription: Optional[str] = None
  itemsName: Optional[List[str]] = None
  taskColor: Optional[str] = None
  isInterval: bool; # true if the task is an interval, false if it is a single task

  startTime: Optional[str] = None # det ska komma in som 990, inte 16:00
  endTime: Optional[str] = None # det ska komma in som 990, inte 16:00
  takesTime: Optional[str] = None #
  travelTime: Optional[str] = None 
  dateOfTask: Optional[str] = None # YYYY-MM-DD format

  icon: Optional[str] = None # The icon that will be shown in the calendar
  travelMode: Optional[str] = None
  googleTask: Optional[bool] = None;
  taken: Optional[bool] = None;


@app.get("/")
def root():
    return {"message": "FastAPI is working!"}


@app.post("/schedule")
def schedule(tasks: List[TaskProps]):
    print(tasks)
    result = scheduler.schedule_tasks(tasks)
    return result
