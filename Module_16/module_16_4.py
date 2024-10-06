from fastapi import FastAPI, HTTPException
import uvicorn
from pydantic import BaseModel

app = FastAPI()

users = []


class User(BaseModel):
    id: int
    username: str
    age: int


@app.get('/users')
async def get_users() -> list[User]:
    return users


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
    uvicorn.run('module_16_4:app', port=8000, reload=True)
