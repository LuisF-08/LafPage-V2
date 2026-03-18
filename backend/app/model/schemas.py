from pydantic import BaseModel, EmailStr

class emailSolicitacao(BaseModel):
    email: EmailStr


class ValidarEmail(BaseModel):
    email: EmailStr
    codigo: str


class ValidarCNPJ(BaseModel):
    cnpj: str