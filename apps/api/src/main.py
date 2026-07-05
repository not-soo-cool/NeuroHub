from fastapi import FastAPI

app = FastAPI(title="NeuroHub API")


@app.get("/health")
async def health():
    return {
        "status": "Kuchh bhi"
    }