from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import Optional, AsyncGenerator

templates = Jinja2Templates(directory='templates')

users = []

class User(BaseModel):
    id: int
    username: str
    age: int
    image_url: Optional[str] = None

async def lifespan(app: FastAPI) -> AsyncGenerator:
    users.append(User(id=1, username="UrbanUser", age=24))
    users.append(User(id=2, username="UrbanTest", age=22))
    users.append(User(id=3, username="Capybara", age=60))
    users.append(User(id=4, username="UrbanWizard", age=40, image_url="image.png"))
    yield

app = FastAPI(lifespan=lifespan)
app.mount("/static", StaticFiles(directory=r"D:\Phyton\Modul_16_5\templates"), name="static")

@app.get('/', response_class=HTMLResponse)
async def get_users(request: Request) -> HTMLResponse:
    return templates.TemplateResponse('main.html', {"request": request, "users": users})

@app.get('/user/{user_id}', response_class=HTMLResponse)
async def get_user(request: Request, user_id: int) -> HTMLResponse:
    if 0 < user_id <= len(users):
        return templates.TemplateResponse('user.html', {"request": request, "user": users[user_id - 1]})
    raise HTTPException(status_code=404, detail="User not found")

@app.post('/user/', response_model=User)
async def create_user(user: User):
    user.id = (users[-1].id + 1) if users else 1
    users.append(user)
    return user

@app.delete('/user/{user_id}')
async def delete_user(user_id: int):
    if 0 < user_id <= len(users):
        return users.pop(user_id - 1)
    raise HTTPException(status_code=404, detail="User not found")