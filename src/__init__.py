from fastapi import FastAPI

from src.users.routes import user_router



app = FastAPI(
    description="AI Smart Glasses"
)

version = "v1"



app.include_router(user_router, prefix=f"/api/{version}/users", tags = ['Users'])
