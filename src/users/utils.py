
from collections import Counter
from src.model import model

async def run_model(img):
    results = model(img)
    detections = results[0].boxes

    labels_idx = [int(cls) for cls in detections.cls]
    labels_name_en = [model.names[idx] for idx in labels_idx]

    labels_name_uz = [COCO_UZ.get(name, name) for name in labels_name_en]

    return dict(Counter(labels_name_uz))

COCO_UZ = {
    "person": "odam",
    "bicycle": "velosiped",
    "car": "mashina",
    "motorcycle": "mototsikl",
    "airplane": "samolyot",
    "bus": "avtobus",
    "train": "poyezd",
    "truck": "yuk mashina",
    "boat": "qayiq",
    "traffic light": "svetofor",
    "fire hydrant": "yong'in krani",
    "stop sign": "to'xtash belgisi",
    "parking meter": "parkovka hisoblagichi",
    "bench": "o‘rindiq",
    "bird": "qush",
    "cat": "mushuk",
    "dog": "it",
    "horse": "ot",
    "sheep": "qo‘y",
    "cow": "sigir",
    "elephant": "fil",
    "bear": "ayiq",
    "zebra": "zebra",
    "giraffe": "jirafa",
    "backpack": "ryukzak",
    "umbrella": "soyabon",
    "handbag": "sumka",
    "tie": "galstuk",
    "suitcase": "chamadon",
    "frisbee": "frisbi",
    "skis": "chang'i",
    "snowboard": "snowboard",
    "sports ball": "to‘p",
    "kite": "varrak",
    "baseball bat": "beysbol tayoqchasi",
    "baseball glove": "qo‘lqop",
    "skateboard": "skateboard",
    "surfboard": "sörf taxtasi",
    "tennis racket": "tennis raketkasi",
    "bottle": "butilka",
    "wine glass": "sharob qadah",
    "cup": "stakan",
    "fork": "vilka",
    "knife": "pichoq",
    "spoon": "qoshiq",
    "bowl": "kosacha",
    "banana": "banan",
    "apple": "olma",
    "orange": "apelsin",
    "broccoli": "brokkoli",
    "carrot": "sabzi",
    "pizza": "pitsa",
    "donut": "donat",
    "cake": "tort",
    "chair": "stul",
    "couch": "divan",
    "bed": "krovat",
    "tv": "televizor",
    "laptop": "noutbuk",
    "mouse": "sichqoncha",
    "keyboard": "klaviatura",
    "cell phone": "telefon",
    "clock": "soat",
    "book": "kitob",
    "scissors": "qaychi",
    "toothbrush": "tish cho‘tkasi"
}