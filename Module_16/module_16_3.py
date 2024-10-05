from fastapi import FastAPI
import uvicorn

app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}


@app.get('/users')
async def get_users() -> dict:
    return users


@app.post('/user/{username}/{age}')
async def add_users(username: str, age: int) -> str:
    new_id = str(int(max(users, key=int)) + 1)
    users[new_id] = 'Имя: {}, возраст: {}'.format(username, age)
    return 'User {} is registered'.format(new_id)


@app.put('/user/{user_id}/{username}/{age}')
async def edit_user(user_id: str, username: str, age: int) -> str:
    users[str(user_id)] = 'Имя: {}, возраст: {}'.format(username, age)
    return 'User {} is registered'.format(user_id)


@app.delete('/user/{user_id}')
async def delete_users(user_id: str) -> str:
    users.pop(user_id)
    return 'User {} deleted'.format(user_id)


if __name__ == '__main__':
    uvicorn.run('module_16_3:app', port=8000, reload=True)
