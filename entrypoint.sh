#!/bin/sh
FRONTEND_PORT=$PORT

echo "frontend port: ${FRONTEND_PORT}"
echo "backend port: ${BACKEND_PORT}"

uvicorn backend:app --host 0.0.0.0 --port $BACKEND_PORT &
streamlit run frontend.py --server.address 0.0.0.0 --server.port $FRONTEND_PORT
