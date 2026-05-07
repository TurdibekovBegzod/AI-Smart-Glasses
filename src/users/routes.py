from fastapi import APIRouter, UploadFile, File
import cv2
import numpy as np
from src.users.utils import run_model
import asyncio
user_router = APIRouter()

@user_router.post("/upload-image")
async def upload_image(file : UploadFile = File(...)):
    
    content = await file.read()
    nparr = np.frombuffer(content, np.uint8)  # bytes → numpy array
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)  # OpenCV bilan o‘qish
    
    label_counts = run_model(img)

    return {
        "label_counts": label_counts   # misol: {"apple": 4, "banana": 5}
    }