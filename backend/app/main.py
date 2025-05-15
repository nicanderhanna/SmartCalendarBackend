from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import List, Optional
#import scheduler as scheduler
from .import scheduler
import json
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional, List, Any



app = FastAPI()
    
class TaskProps(BaseModel):
  id: Optional[str] = None #this will be assigned by firebase

  taskName: Optional[str] = None
  contactName: Optional[str] = None
  taskDescription: Optional[str] = None
  itemsName: Optional[List[str]] = None
  taskColor: Optional[str] = None

  startTime: Optional[str] = None 
  endTime: Optional[str] = None # 
  takesTime: Optional[str] = None 
  travelTime: Optional[Any] = None 
  dateOfTask: Optional[str] = None # YYYY-MM-DD format

  origin: Optional[Any] = None
  destination: Optional[Any] = None
  icon: Optional[str] = None # The icon that will be shown in the calendar
  travelMode: Optional[str] = None
  googleTask: Optional[bool] = None
  taken: Optional[bool] = None

  scheduledStartTime: Optional[str] = None # The time the schedule API has decided is best
  scheduledEndTime: Optional[str] = None

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {"message": "FastAPI is working!"}

@app.post("/schedule")
def schedule(tasks: List[TaskProps]):
    try:
        result = scheduler.schedule_tasks(tasks)
        return result
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)