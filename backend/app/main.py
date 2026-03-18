from fastapi import FastAPI
from app.routes import autenticacao
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(autenticacao.router)

@app.get("/")
def inicio():
    return { 'message' : 'SERVER ESTÁ ON ╰(*°▽°*)╯'}