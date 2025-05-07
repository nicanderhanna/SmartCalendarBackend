from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional
#import scheduler as scheduler
from .import scheduler
import json

app = FastAPI()
    
class TaskProps(BaseModel):
  id: Optional[str] = None #this will be assigned by firebase

  taskName: Optional[str] = None
  contactName: Optional[str] = None
  taskDescription: Optional[str] = None
  itemsName: Optional[List[str]] = None
  taskColor: Optional[str] = None
  isInterval: bool # true if the task is an interval, false if it is a single task

  startTime: Optional[str] = None 
  endTime: Optional[str] = None # 
  duration: Optional[str] = None 
  travelTime: Optional[str] = None 
  dateOfTask: Optional[str] = None # YYYY-MM-DD format

  icon: Optional[str] = None # The icon that will be shown in the calendar
  travelMode: Optional[str] = None
  googleTask: Optional[bool] = None
  taken: Optional[bool] = None

@app.get("/")
def root():
    return {"message": "FastAPI is working!"}

@app.post("/schedule")
def schedule(tasks: List[TaskProps]):
    try:
        print("this is before!!!!!!!!!!!!!")
        print(tasks)
        result = scheduler.schedule_tasks(tasks)
        print("this is after!!!!!!!!!!!!!")
        print(json.dumps(result))
        return result
    except Exception as e:
        print("❌ Fel i /schedule:", e)
        return JSONResponse(content={"error": str(e)}, status_code=500)