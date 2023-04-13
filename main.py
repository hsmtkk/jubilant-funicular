import dotenv
from fastapi import FastAPI

import routers.todo

dotenv.load_dotenv()

app = FastAPI()

app.include_router(routers.todo.router)
