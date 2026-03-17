from fastapi import FastAPI
from app.routes import autenticacao

app = FastAPI()

app.include_router(router=autenticacao)