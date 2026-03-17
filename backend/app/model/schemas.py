from pydantic import BaseModel


class emailSolicitacao(BaseModel):
    email : str


class ValidarEmail(BaseModel):
    email: str
    codigo: str