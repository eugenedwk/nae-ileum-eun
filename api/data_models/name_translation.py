from pydantic import BaseModel
from typing import List

class NamePair(BaseModel):
    english: str
    complement: str

class TranslationRequest(BaseModel):
    language: str = "kor"
    name_pair: NamePair
    
class PhoneticTokenTranslation(BaseModel):
    input_token: str
    output_token: str

class TranslationResponse(BaseModel):
    translation: List[PhoneticTokenTranslation] 