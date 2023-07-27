from pydantic import BaseModel

class KoreanName(BaseModel):
    romanized_english: str
    korean_parallel: str | None = None
    