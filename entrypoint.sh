#!/bin/sh
FRONTEND_PORT=$PORT
uvicorn backend:app --reload --host 0.0.0.0 --port $BACKEND_PORT &
streamlit run frontend.py --server.address 0.0.0.0 --server.port $FRONTEND_PORT
