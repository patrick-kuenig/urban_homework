from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get('/')
async def main() -> dict:
    return {'message': 'Главная страница'}

@app.get('/user/admin')
async def admin() -> dict:
    return {'message': 'Вы вошли как администратор'}

@app.get('/user/{user_id}')
async def user_with_id(user_id) -> dict:
    return {'message': f'Вы вошли как пользователь № {user_id}'}

@app.get('/user/')
async def username_age(username, age) -> dict:
    return {'message': f'Информация о пользователе. Имя {username}, Возраст: {age}'}


if __name__ == '__main__':
    uvicorn.run('module_6_1:app', port=8000, reload=True)