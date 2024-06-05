from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def home() -> dict[str,str]:
    return {"status":"Api running"}
