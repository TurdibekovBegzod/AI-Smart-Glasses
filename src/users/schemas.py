from pydantic import BaseModel


class ImageToText(BaseModel):
    image_byte : bytes