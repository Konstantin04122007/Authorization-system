import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import FileResponse
from starlette.staticfiles import StaticFiles


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class User(BaseModel):
    username: str
    email: str
    phone: int
    password: str
    country: str


@app.post("/users/")
async def get_data(user: User):
    return FileResponse("templates/users.html")


app.mount("/users", app)
app.mount("/", StaticFiles(directory="templates", html=True))


if __name__ == '__main__':
    uvicorn.run(app, host='localhost', port=8000)
