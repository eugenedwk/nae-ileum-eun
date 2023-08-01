from pydantic import BaseModel
from typing import List

class KoreanName(BaseModel):
    romanized_english: str
    korean_parallel: str

class PhoneticTranslation(BaseModel):
    input: str
    output: str

class TranslationAPIResponse(BaseModel):
    korean_name: KoreanName
    translation: List[PhoneticTranslation] 