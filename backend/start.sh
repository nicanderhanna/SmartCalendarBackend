#!/bin/bash

# Starta FastAPI med uvicorn på Render-vänligt sätt
uvicorn main:app --host=0.0.0.0 --port=10000