from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import json
from fastapi.responses import HTMLResponse

app = FastAPI() # <- Создаем экземпляр класса FastAPI
templates = Jinja2Templates(directory="templates")

def database(name_db, mode, data=None):
    if mode == 'r':
        with open(name_db, mode, encoding='utf-8') as db:
            return json.load(db)
    elif mode == 'r+':
        with open(name_db, mode, encoding='utf-8') as db:
            json.dump(data, db)
            

@app.get("/tasks/")
def get_tasks(request:Request):
    data = database('database.json', 'r')
    
    return templates.TemplateResponse(request=request, name='task_list.html', context=data)

class Task(BaseModel):
    title:str
    description:str

@app.post("/tasks/")
def post_task(request:Request, task:Task):
    title = task.title
    desc = task.description
    dict_copy = {"title":title, "description": desc}
    print(dict_copy)
    with open('database.json', 'r', encoding='utf-8') as db:
        data = json.load(db)
        data["tasks"].append(dict_copy)
        print(data)
        with open('database.json', 'w', encoding='utf-8') as db_clear:
            #json.dumps(data)
            json.dump(data, db_clear, indent=4, ensure_ascii=False)
    return templates.TemplateResponse(request=request, name='task_list.html', context=data)
        

# uvicorn main:app --reload
# python -m venv venv
# .\venv\Scripts\activate
# pip install -U -r requirements.txt