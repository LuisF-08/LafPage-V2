from fastapi import APIRouter,Form, File, UploadFile, Depends, BackgroundTasks
from app.model.models import emailSolicitacao,ValidarEmail,ValidarCNPJ,ValidarNotaFiscal
from app.services.email_services import enviar_email_codigo,validar_codigo
from app.services.cnpj_service import validar_cnpj
from app.services.sac_service import processar_formulario_sac
from app.services.conexao_sac import listar_sac, validar_cnpj_banco, validar_nota_fiscal_banco
from app.database.database import get_db
from sqlalchemy.orm import Session


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

@router.get("/sac")
def listar_sac_route():
    return listar_sac()

@router.post("/validar-cnpj-banco")
def buscar_cnpj_no_banco(data: ValidarCNPJ):
    return validar_cnpj_banco(data.cnpj)   

@router.post("/validar-nota-fiscal") 
def buscar_nota_fiscal_no_banco(data: ValidarNotaFiscal):
    return validar_nota_fiscal_banco(data.nota_fiscal)

@router.post("/sac-envio")
async def criar_formulario_sac(
    background_tasks: BackgroundTasks,dados: str = Form(...),
    arquivo: UploadFile = File(None),db: Session = Depends(get_db)):
    response = await processar_formulario_sac(dados,arquivo,db,background_tasks)
    return response