from fastapi import APIRouter
from app.model.schemas import emailSolicitacao,ValidarEmail
from app.services.email_services import enviar_email_codigo,validar_codigo

router = APIRouter()

router.post("/enviar-codigo")
async def enviar(data: emailSolicitacao):
    return await enviar_email_codigo(data.email)

router.post("/validar-codigo")
async def validar(data: ValidarEmail):
    return await validar_codigo(data.codigo)