# uvicorn app.main:app --reload


from fastapi import FastAPI
from app.routers import task, user

app = FastAPI()

@app.get("/")
async def welcome():
    print(123454)
    return {"message": "Welcome to Taskmanadger"}

app.include_router(task.router)
app.include_router(user.router)


#if __name__ == '__main__':
#   uvicorn.run(app.main:app, host='127.0.0.1', port=8000, log_level='info')



