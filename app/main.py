from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

app = FastAPI() # <- Создаем экземпляр класса FastAPI
templates = Jinja2Templates(directory="templates")

@app.get("/") # <- декоратор, который обрабатывает get - запросы где маршрут
def index(request: Request):
    return templates.TemplateResponse(request=request, name='index.html')

class Item(BaseModel):
    login: str
    password: str

@app.post('/')
def index_post(request:Request, item:Item):
    print(item)
    return templates.TemplateResponse(request=request, name='index.html', context=item)

@app.get("/login/") # <- декоратор, который обрабатывает get - запросы где маршрут
def login(request:Request):
    return templates.TemplateResponse(request=request, name="login.html") 

@app.get("/tasks/") # <- декоратор, который обрабатывает get - запросы где маршрут
def tasks(request:Request):
    context = {"task": "Купить молоко"}
    return templates.TemplateResponse(request=request, name="tasks.html", context=context)

# uvicorn main:app --reload
# python -m venv venv
# .\venv\Scripts\activate
# pip install -U -r requirements.txt