from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from dotenv import load_dotenv

load_dotenv()
HOST = os.getenv("DB_HOST")
BANCO = os.getenv("DB_DATABASE")
USUARIO = os.getenv("DB_USER")
SENHA = os.getenv("DB_PASSWORD")

DATABASE_URL = f"postgresql://{USUARIO}:{SENHA}@{HOST}/{BANCO}"
Base = declarative_base()
engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
