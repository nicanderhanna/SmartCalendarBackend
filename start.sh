#!/bin/bash

# Starta FastAPI med uvicorn på Render-vänligt sätt
uvicorn app.main:app --host=0.0.0.0 --port=$PORT