from fastapi import FastAPI
from app.routes import autenticacao
from app.middleware.middleware import  setup_middleware

app = FastAPI()

setup_middleware(app)

app.include_router(autenticacao.router)

@app.get("/")
def inicio():
    return { 'message' : 'SERVER ESTÁ ON ╰(*°▽°*)╯'}