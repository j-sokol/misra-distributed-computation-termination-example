#!/bin/bash
set -eux
# MODULE_NAME=manage
# VARIABLE_NAME=${VARIABLE_NAME:-app}
# export APP_MODULE=${APP_MODULE:-"$MODULE_NAME:$VARIABLE_NAME"}

# DEFAULT_GUNICORN_CONF=./gunicorn.conf.py

# export GUNICORN_CONF=${GUNICORN_CONF:-$DEFAULT_GUNICORN_CONF}

# Start Gunicorn
if [ -f /.dockerenv ]; then
    # Inside docker
    # exec gunicorn --worker-tmp-dir /dev/shm -k egg:meinheld#gunicorn_worker -c "$GUNICORN_CONF" "$APP_MODULE"
    uvicorn distributedapp.main:app --host 0.0.0.0 --port 5049  --log-level debug
else
    # exec gunicorn  -k egg:meinheld#gunicorn_worker -c "$GUNICORN_CONF" "$APP_MODULE"
    uvicorn distributedapp.main:app --host 0.0.0.0 --port 5049  --log-level debug
fi
