
from collections import Counter
from src.model import model
from src.users.translate import COCO_UZ
def run_model(img):
    results = model(img)
    detections = results[0].boxes

    labels_idx = [int(cls) for cls in detections.cls]
    labels_name_en = [model.names[idx] for idx in labels_idx]

    labels_name_uz = [COCO_UZ.get(name, name) for name in labels_name_en]

    return dict(Counter(labels_name_uz))

