import dotenv
from fastapi import FastAPI

import routers.todo
import routers.user

dotenv.load_dotenv()

app = FastAPI()

app.include_router(routers.todo.router)
app.include_router(routers.user.router)
