This is the backend service for the Smart Calendar application. 
It is responsible for scheduling tasks and calculating the best 
available time slots based on the constraints of each task. 
The backend is built with Python using FastAPI (or Flask if applicable) 
and is deployed on Render.com. 

It exposes a single main endpoint: 
POST /schedule. 

This endpoint accepts a list of tasks in JSON format, where each task includes 
properties such as id, taskName, isInterval, duration, dateOfTask, 
and other optional metadata. 
The response returns the same tasks, now updated with the scheduledStartTime 
and scheduledEndTime fields indicating the proposed time slot for each task. 

To run the backend locally, clone the repository, 
create and activate a virtual environment, 
install dependencies using pip install -r requirements.txt, 
and start the server with uvicorn main:app --reload. 

The backend will be available at http://localhost:8000. 
The production version is hosted at https://smartcalendarbackend.onrender.com/, 
where the /schedule endpoint can be tested using tools like Postman or cURL.