from fastapi import FastAPI
from ultralytics import YOLO
from src.users.routes import user_router


model = YOLO("yolov8m.pt")

app = FastAPI(
    description="AI Smart Glasses"
)

version = "v1"



app.include_router(user_router, prefix=f"/api/{version}/users", tags = ['Users'])
