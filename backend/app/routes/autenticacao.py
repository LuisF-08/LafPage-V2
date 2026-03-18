from fastapi import APIRouter
from app.model.schemas import emailSolicitacao,ValidarEmail,ValidarCNPJ
from app.services.email_services import enviar_email_codigo,validar_codigo
from app.services.cnpj_service import validar_cnpj

router = APIRouter()

@router.post("/enviar-codigo")
async def enviar(data: emailSolicitacao):
    return await enviar_email_codigo(data.email)


@router.post("/validar-codigo")
async def validar(data: ValidarEmail):
    return validar_codigo(data.email, data.codigo)

@router.post("/validar-cnpj")
async def validar(data: ValidarCNPJ):
    return await validar_cnpj(data.cnpj)