from pydantic import BaseModel
from typing import List

class KoreanName(BaseModel):
    romanized_english: str
    korean_parallel: str

class PhoneticTokenTranslation(BaseModel):
    input_token: str
    output_token: str

class TranslationAPIResponse(BaseModel):
    korean_name: KoreanName
    translation: List[PhoneticTokenTranslation] 