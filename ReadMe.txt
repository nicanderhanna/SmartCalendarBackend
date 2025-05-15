# Smart Calander Backend v 0.1

This is the backend service for the Smart Calendar application. 
It is responsible for scheduling tasks and calculating the best 
available time slots based on the constraints of each task. 
The backend is built with Python using FastAPI and is deployed on Render.com. 

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

## Contact / Support
**Main Contact: Hanna Nicander, hanna.nicander@hotmail.com**
Reach us:
- Project owner: Joel Friis, p.lars.joelfriis@gmail.com
- Scrum master: Hanna Nicander, hanna.nicander@hotmail.com
- Developer: Alexander Alvarez, alealv04@hotmail.com
- Developer: Andia Mir, andiamir52@gmail.com
- Developer: Daniella Rönnlund, dronn@kth.se
- Developer: Dante Consentino, djco@kth.se
- Developer: Linnea Udén, linnea.uden1@gmail.com
- Developer: Nikodemus Ohm, nikno@kth.se