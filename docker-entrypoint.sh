#!/bin/bash
set -eux

# Start Gunicorn
if [ -f /.dockerenv ]; then
    uvicorn distributedapp.main:app --host 0.0.0.0 --port 5049  --log-level debug
else
    uvicorn distributedapp.main:app --host 0.0.0.0 --port 5049  --log-level debug
fi
