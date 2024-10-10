from fastapi import FastAPI
from routers import task
from routers import user
import uvicorn

app = FastAPI()


@app.get('/')
async def welcome_message():
    return {'message': 'Welcome to Taskmanager'}

app.include_router(task.router)
app.include_router(user.router)


if __name__ == '__main__':
    uvicorn.run('main:app', port=8000, reload=True)