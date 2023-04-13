#!/bin/sh
STREAMLIT_PORT=$PORT

echo "frontend port: ${STREAMLIT_PORT}"
echo "backend port: ${FASTAPI_PORT}"

uvicorn backend:app --host 0.0.0.0 --port $FASTAPI_PORT &
streamlit run frontend.py --server.address 0.0.0.0 --server.port $STREAMLIT_PORT
