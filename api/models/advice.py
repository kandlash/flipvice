from pydantic import BaseModel

class Advice(BaseModel):
    id: int
    title: str
    advice: str
    description: str
    tags: list[str]