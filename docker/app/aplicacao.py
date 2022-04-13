from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
async def health():
    return{
        "statusCode": 200,
        "message": "ok"
    }