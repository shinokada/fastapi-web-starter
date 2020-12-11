from fastapi import FastAPI, Request, Form, APIRouter
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import os

router = APIRouter()
templates = Jinja2Templates(directory="templates/")


@router.get("/twoforms", response_class=HTMLResponse)
def form_get(request: Request):
    key = os.getenv("unsplash_key")
    print(key)
    result = "Type a number"
    return templates.TemplateResponse('twoforms.html', context={'request': request, 'result': result})


@router.post("/form1", response_class=HTMLResponse)
def form_post1(request: Request, number: int = Form(...)):
    result = number + 2
    return templates.TemplateResponse('twoforms.html', context={'request': request, 'result': result, 'yournum': number})


@router.post("/form2", response_class=HTMLResponse)
def form_post2(request: Request, number: int = Form(...)):
    result = number + 100
    return templates.TemplateResponse('twoforms.html', context={'request': request, 'result': result, 'yournum': number})
