from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/")
async def home():
    data = {
        "text": "hi"
    }
    return {"data": data}


@app.get("/page/{page_name}")
async def page(page_name: str):
    data = {
        "page": page_name
    }
    return {"data": data}
