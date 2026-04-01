from fastapi.responses import StreamingResponse
from fastapi import HTTPException
from pytrustnfe.nfe.danfe import danfe
import xml.etree.ElementTree as ET
import xml.dom.minidom
from app.schemas.schema import SegundaViaNotaFiscal
import io
import logging



async def baixar_nota_fiscal_pdf(cnpj: str, db):
    nota = db.query(SegundaViaNotaFiscal).filter(
        SegundaViaNotaFiscal.cnpj == cnpj
    ).first()

    if not nota or not nota.xml:
        raise HTTPException(404, "Nota não encontrada")

    try:
        xml_bytes = nota.xml if isinstance(nota.xml, bytes) else nota.xml.encode("utf-8")

        pdf = danfe(xml_bytes)

        if pdf is None:
            raise ValueError("danfe() retornou None")

        buffer = io.BytesIO(pdf)
        buffer.seek(0)

        return StreamingResponse(
            buffer,
            media_type="application/pdf",
            headers={
                "Content-Disposition": f"attachment; filename=nfe_{nota.nfe}.pdf"
            }
        )

    except HTTPException:
        raise
    except Exception as e:
        logger.exception(f"Erro ao gerar DANFE para CNPJ {cnpj}")
        raise HTTPException(500, f"Erro ao gerar DANFE: {str(e)}")

async def obter_xml_formatado(cnpj: str, db):
    nota = db.query(SegundaViaNotaFiscal).filter(
        SegundaViaNotaFiscal.cnpj == cnpj
    ).first()

    if not nota:
        raise HTTPException(404, "Nota não encontrada")

    try:
        dom = xml.dom.minidom.parseString(nota.xml)
        xml_bonito = dom.toprettyxml(indent="  ")
    except:
        xml_bonito = nota.xml
    
    return {
        "cnpj": nota.cnpj,
        "nfe": nota.nfe,
        "xml": xml_bonito
    }