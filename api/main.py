import uvicorn
from fastapi import FastAPI
from data_models.name_translation import KoreanName

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
async def translate(name:KoreanName) -> dict:
    """Function to handle /translation POST request endpoint

    Args:
        name (KoreanName): name with english romanization and korean parallel

    Returns:
        dict: JSON response payload as dictionary
    """
    print(f"/translation/ called with POST Request Body:\n{' '*4}{name}")
    ## TODO: Add code below to take in name and return a pronounciation string


    return {
        "message": f"POST Request for { name.romanized_english } received"
    }

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)