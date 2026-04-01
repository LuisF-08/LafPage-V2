from fastapi import APIRouter, Form, File, UploadFile, Depends, BackgroundTasks, HTTPException
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.model.models import (emailSolicitacao,ValidarEmail,ValidarCNPJ,ValidarNotaFiscal)
from app.services.email_services import enviar_email_codigo, validar_codigo
from app.services.cnpj_service import validar_cnpj
from app.services.nota_fiscal_service import baixar_nota_fiscal_pdf
from app.services.sac_service import processar_formulario_sac
from app.services.boleto_service import  gerar_pdf_bytes
from app.services.conexao_sac import validar_cnpj_banco, validar_nota_fiscal_banco
from fastapi.responses import StreamingResponse
from fastapi import HTTPException
from app.schemas.schema import SegundaViaNotaFiscal,Boleto
import xml.dom.minidom
from fastapi import Response
from sqlalchemy import desc, cast, Date

from typing import Optional

router = APIRouter()

# =========================
# 📧 EMAIL
# =========================
@router.post("/enviar-codigo")
async def enviar(data: emailSolicitacao):
    return await enviar_email_codigo(data.email)


@router.post("/validar-codigo")
async def validar(data: ValidarEmail):
    return validar_codigo(data.email, data.codigo)

# =========================
# 🏢 CNPJ
# =========================
@router.post("/validar-cnpj")
async def validar(data: ValidarCNPJ):
    return await validar_cnpj(data.cnpj)

@router.post("/validar-cnpj-banco")
def buscar_cnpj_no_banco(data: ValidarCNPJ):
    return validar_cnpj_banco(data.cnpj)

# =========================
# 📄 NOTA FISCAL
# =========================
@router.post("/validar-nota-fiscal")
def buscar_nota_fiscal_no_banco(data: ValidarNotaFiscal):
    return validar_nota_fiscal_banco(data.nota_fiscal)


@router.post("/sac-envio")
async def criar_formulario_sac(
    background_tasks: BackgroundTasks,
    dados: str = Form(...),
    arquivo: UploadFile = File(None),
    db: Session = Depends(get_db)
):
    return await processar_formulario_sac(dados, arquivo, db, background_tasks)


@router.get("/baixar-pdf/{cnpj}",response_class=StreamingResponse,responses={200: {"content": {"application/pdf": {}},
            "description": "PDF da nota fiscal" }})
async def baixar_pdf(cnpj: str, db: Session = Depends(get_db)):
    return await baixar_nota_fiscal_pdf(cnpj, db)


@router.get("/baixar-xml/{cnpj}")
async def baixar_xml_formatado(cnpj: str, db: Session = Depends(get_db)):
    nota = db.query(SegundaViaNotaFiscal).filter(
        SegundaViaNotaFiscal.cnpj == cnpj
    ).first()
    if not nota:
        raise HTTPException(404, "Nota não encontrada")
    try:
        dom = xml.dom.minidom.parseString(nota.xml)
        xml_bonito = dom.toprettyxml(indent="  ")
    except Exception:
        xml_bonito = nota.xml
    nome_arquivo = f"nota_{nota.nfe if nota.nfe else cnpj}.xml"
    return Response(
        content=xml_bonito, 
        media_type="application/xml",
        headers={"Content-Disposition": f"attachment; filename={nome_arquivo}"
        }
    )
    
@router.get("/notas/{cnpj}")
async def buscar_notas_fiscais(cnpj: str, db: Session = Depends(get_db)):
    notas = db.query(SegundaViaNotaFiscal).filter(
        SegundaViaNotaFiscal.cnpj == cnpj
    ).all()
    return notas

@router.get("/notas/{cnpj}")
async def buscar_notas_e_numeros(cnpj: str, nfe: Optional[str] = None, numero_pedido: Optional[int] = None, db: Session = Depends(get_db)):
    query = db.query(SegundaViaNotaFiscal).filter(SegundaViaNotaFiscal.cnpj == cnpj)
    if nfe:
        query = query.filter(SegundaViaNotaFiscal.nfe == nfe)
    if numero_pedido:
        query = query.filter(SegundaViaNotaFiscal.numero_pedido == numero_pedido)
    query = query.order_by(desc(SegundaViaNotaFiscal.criado_em))
    return query.all()

@router.get("/validar-boleto/{codigo_de_barras}")
async def validar_boleto_rota(codigo_de_barras: str, db: Session = Depends(get_db)):
    boleto = db.query(Boleto).filter(Boleto.codigo_de_barras == codigo_de_barras).first()
    if not boleto:
        raise HTTPException(status_code=404, detail="Boleto não encontrado no banco de dados.")
    return boleto

@router.get("/baixar-pdf-boleto/{boleto_id}")
async def baixar_pdf_rota(boleto_id: int, db: Session = Depends(get_db)):
    boleto = db.query(Boleto).filter(Boleto.id == boleto_id).first()
    if not boleto:
        raise HTTPException(404, "Erro ao localizar o boleto para download.")
    pdf_buffer = gerar_pdf_bytes(boleto)
    return StreamingResponse(
        pdf_buffer,
        media_type="application/pdf",
        headers={"Content-Disposition": f"attachment; filename=boleto_lafmed_{boleto_id}.pdf"}
    )

@router.get("/buscar-boletos/{cnpj}")
async def buscar_boletos_por_cnpj(
    cnpj: str,
    id: Optional[int] = None,        
    criado_em: Optional[str] = None,  
    db: Session = Depends(get_db)
):
    query = db.query(Boleto).filter(Boleto.cnpj == cnpj)

    if id:
        query = query.filter(Boleto.id == id)
    if criado_em:
        query = query.filter(cast(Boleto.criado_em, Date) == criado_em)

    return query.order_by(desc(Boleto.criado_em)).all()  