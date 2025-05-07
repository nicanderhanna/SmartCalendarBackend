#!/bin/bash

pip install -r requirements.txt

# Starta FastAPI med uvicorn på Render-vänligt sätt
uvicorn backend.app.main:app --host=0.0.0.0 --port=$PORT

#uvicorn backend.app.main:app --reload