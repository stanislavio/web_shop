from fastapi import FastAPI

from src.users.list import router

app = FastAPI()

app.include_router(prefix='/api/v1', router=router)
