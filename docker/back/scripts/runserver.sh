#!/bin/bash

set -eu
cd "$(dirname "$0")/.."

if [ -z "${PROJECT_ENV+x}" ]; then
  PROJECT_ENV=local
  # uvicorn main:app --workers 1 --reload --host 0.0.0.0 --port 8000
fi

UVICORN_OPTIONS="--host 0.0.0.0 --port 8000"
WORKERS="${BACKEND_UVICORN_WORKERS}"

if [ "${PROJECT_ENV}" = "production" ] ;then
  WORKERS="${BACKEND_UVICORN_WORKERS_PRODUCTION}"
  UVICORN_COMMAND="uvicorn main:app --workers ${WORKERS} ${UVICORN_OPTIONS}"
elif [ "${PROJECT_ENV}" = "staging" ]; then
  WORKERS="${BACKEND_UVICORN_WORKERS_STAGING}"
  UVICORN_COMMAND="uvicorn main:app --workers ${WORKERS} ${UVICORN_OPTIONS}"
elif [ "${PROJECT_ENV}" = "develop" ]; then
  WORKERS="${BACKEND_UVICORN_WORKERS_DEVELOP}"
  UVICORN_COMMAND="uvicorn main:app --workers ${WORKERS} ${UVICORN_OPTIONS}"
else
  UVICORN_COMMAND="uvicorn main:app --workers ${WORKERS} --reload ${UVICORN_OPTIONS}"
fi
echo "trying workers=${WORKERS} options=${UVICORN_OPTIONS}"

cd src && ${UVICORN_COMMAND}
