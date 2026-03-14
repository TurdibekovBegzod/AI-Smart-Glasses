from fastapi import APIRouter, UploadFile, File
import cv2
import numpy as np
from collections import Counter


user_router = APIRouter()

@user_router.post("/upload-image")
async def upload_image(file : UploadFile = File(...)):
    from src import model
    content = await file.read()
    nparr = np.frombuffer(content, np.uint8)  # bytes → numpy array
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)  # OpenCV bilan o‘qish
    
    results = model(img)
    detections = results[0].boxes

    labels_idx = [int(cls) for cls in detections.cls]              # class indexlari
    labels_name = [model.names[idx] for idx in labels_idx]         # class nomlari

    

    # Nechta topilganini hisoblash
    label_counts = dict(Counter(labels_name))

    return {
        "label_counts": label_counts   # misol: {"apple": 4, "banana": 5}
    }
        
