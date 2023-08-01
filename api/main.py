import uvicorn
from fastapi import FastAPI
from data_models.name_translation import (
    KoreanName, 
    PhoneticTranslation,
    TranslationAPIResponse
)

app = FastAPI()

@app.get("/")
async def root() -> dict:
    """Function to handle root endpoint for API.
    Current behavior returns 'Hello World' string.

    Returns:
        dict: JSON response payload as dictionary
    """
    return { 
        "message": "Hello World" 
    }

@app.post("/translation/")
async def translate(name:KoreanName) -> TranslationAPIResponse:
    """Function to handle /translation POST request endpoint

    Args:
        name (KoreanName): name with english romanization and korean parallel

    Returns:
        TranslationAPIResponse: JSON response payload as dictionary
    """
    ## TODO: Add code below to take in name and return a pronounciation string
    
    # temporary placeholder for actual translation/phonetic spelling process
    temp_kor = ["가","나","다","라","마","바","사","아","자","차","카","타","파","하"]
    temp_eng = ["Gah","Nah","Dah","Rah","Mah","Bah","Sah","Ah","Jah","Chah","Kah","Tah","Pah","Hah"]

    phonetic_li = []
    for i in range(len(name.korean_parallel)):
        phonetic_li.append(
            PhoneticTranslation(
                input=name.korean_parallel[i],
                output=temp_eng[i]
            )
        )
    
    # create and return a translation response
    resp = TranslationAPIResponse(
        korean_name=name,
        translation=phonetic_li
    )
    print(resp)
    return resp

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)