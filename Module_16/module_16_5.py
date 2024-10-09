from fastapi import FastAPI, HTTPException, Body, Request, Form
from fastapi.responses import Response, HTMLResponse
import uvicorn
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory='templates')
app = FastAPI()

users = []


class User(BaseModel):
    id: int
    username: str
    age: int


@app.get('/')
async def get_users(request: Request) -> templates.TemplateResponse:
    return templates.TemplateResponse('users.html', {'request': request, 'users': users})


@app.get('/users/{user_id}')
async def get_user(request: Request, user_id: int) -> templates.TemplateResponse:
    try:
        return templates.TemplateResponse('users.html', {'request': request, 'user': users[user_id]})
    except IndexError:
        raise HTTPException(status_code=404, detail='User not found')

@app.post('/user/{username}/{age}')
async def add_user(user: User) -> User:
    user.id = len(users)
    users.append(user)
    return user


@app.put('/user/{user_id}/{username}/{age}')
async def edit_user(user: User) -> str:
    try:
        users[user.id] = user
        return 'User {} is registered'.format(user.id)
    except IndexError:
        raise HTTPException(status_code=404, detail='User not found')


@app.delete('/user/{user_id}')
async def delete_users(user_id: int) -> str:
    try:
        users.pop(user_id)
        return 'User {} deleted'.format(user_id)
    except IndexError:
        raise HTTPException(status_code=404, detail='User not found')


if __name__ == '__main__':
    uvicorn.run('module_16_5:app', port=8000, reload=True)
