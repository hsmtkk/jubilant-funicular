#!/bin/sh
BACKEND_PORT=`eval $PORT + 10000`

echo "frontend port: ${PORT}"
echo "backend port: ${BACKEND_PORT}"

uvicorn backend:app --host 0.0.0.0 --port $BACKEND_PORT &
streamlit run frontend.py --server.address 0.0.0.0 --server.port $PORT
