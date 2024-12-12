from pydantic import BaseModel

class Advice(BaseModel):
    title: str
    advice: str
    description: str
    tags: list[str]