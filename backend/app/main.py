from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional
import json
from flask import Flask, request, jsonify
from scheduler import schedule_tasks
    
app = FastAPI()


@app.get("/")
def root():
    return {"message": "FastAPI is working!"}


app = Flask(__name__)


@app.route('/schedule', methods=['POST'])
def schedule():
    tasks = request.json  # array of TaskProps
    result = schedule_tasks(tasks)
    return jsonify(result)


if __name__ == '__main__':
    app.run()
