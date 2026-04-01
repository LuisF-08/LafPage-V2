import json
import os
import uuid
from fastapi import HTTPException, BackgroundTasks
from app.schemas.schema import SACFormulario,SACItem
from email.message import EmailMessage
import smtplib
from dotenv import load_dotenv

load_dotenv()

EMAIL_REMETENTE = os.getenv("EMAIL_USER")
SENHA_APP = os.getenv("EMAIL_PASS")

UPLOAD_DIR = "uploads"
MAX_SIZE = 1 * 1024 * 1024  # 1MB
ALLOWED_TYPES = ["image/jpeg", "image/png", "application/pdf"]



async def processar_formulario_sac(dados, 
                                arquivo,
                                db,
                                background_tasks: BackgroundTasks):
    
    # Converter JSON
    try:
        dados = json.loads(dados)
    except:
        raise HTTPException(status_code=400, detail="JSON inválido")

    # Validação manual (IMPORTANTE)
    campos_obrigatorios = [
        "nome", "email", "contato",
        "nota_fiscal", "assunto",
        "problema", "descricao", "itens"
    ]

    for campo in campos_obrigatorios:
        if campo not in dados:
            raise HTTPException(status_code=400, detail=f"Campo obrigatório: {campo}")

    #  Upload arquivo
    caminho_final = None

    if arquivo and arquivo.filename:
        if arquivo.content_type not in ALLOWED_TYPES:
            raise HTTPException(status_code=400, detail="Tipo de arquivo inválido")

        os.makedirs(UPLOAD_DIR, exist_ok=True)

        nome_unico = f"{uuid.uuid4()}_{os.path.basename(arquivo.filename)}"
        caminho_final = os.path.join(UPLOAD_DIR, nome_unico)

        tamanho = 0
        with open(caminho_final, "wb") as f:
            while chunk := await arquivo.read(1024):
                tamanho += len(chunk)
                if tamanho > MAX_SIZE:
                    raise HTTPException(status_code=400, detail="Arquivo muito grande")
                f.write(chunk)

    itens_para_banco = []

    for item in dados["itens"]:
        novo_item_db = SACItem(
            produto_id=item["id"],
            nome_produto=item["nome_produto"],
            quantidade_original=item["quantidade_original"],
            quantidade_devolucao=item["quantidade_devolucao"]
        )
        itens_para_banco.append(novo_item_db)
    
    # cria formulario 
    sac = SACFormulario(
        nome=dados["nome"],
        email=dados["email"],
        contato=dados["contato"],
        nota_fiscal=dados["nota_fiscal"],
        assunto=dados["assunto"],
        problema=dados["problema"],
        descricao=dados["descricao"],
        arquivo=caminho_final
    )
    sac.itens = itens_para_banco  

    try:
        db.add(sac)
        db.commit()
        db.refresh(sac)
        print("DADOS COMPLETOS:", dados)
        print("ITENS RECEBIDOS:", dados.get("itens"))
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Erro ao salvar: {str(e)}")

    # Envio de email para o sac Email
    background_tasks.add_task(enviar_email_sac, dados, sac.id, caminho_final)

    return {"ok": True, "id": sac.id}



def enviar_email_sac(form, sac_id, caminho_arquivo=None):
    msg = EmailMessage()
    msg["Subject"] = f"📩 Novo SAC - {form['assunto']}"
    msg["From"] = EMAIL_REMETENTE
    msg["To"] = form["email"]
    

    html = f"""
    <html>
<head>
    <meta charset="UTF-8">
    </head>
    <body style="font-family: 'Segoe UI', Arial, sans-serif;
    background-color: #f8fafc; color: #334155; margin: 0; padding: 40px;">
        <div style="max-width: 700px; margin: auto;
        background: white; border: 1px solid #e2e8f0; border-radius: 8px;
        box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1);">
            
            <div style="padding: 30px; border-bottom: 2px solid #f1f5f9;">
                <h1 style="margin: 0; color: #1e40af;
                font-size: 20px; text-transform: uppercase; letter-spacing: 1px;">Chamado SAC Devolução de Mercadoria</h1>
                <p style="margin: 5px 0 0; color: #64748b
                ; font-size: 14px;">Protocolo: <strong>#{sac_id}</strong></p>
            </div>
    
            <div style="padding: 30px;">
                <h2 style="font-size: 16px; color: #334155;
                border-left: 4px solid #2563eb; padding-left: 10px; margin-bottom: 15px;">Informações do Cliente</h2>
                <table style="width: 100%; font-size: 14px; 
                border-collapse: collapse; margin-bottom: 25px;">
                    <tr>
                        <td style="padding: 5px 0; color: #64748b; width: 120px;">Nome:</td>
                        <td style="padding: 5px 0; font-weight: 600;">{form['nome']}</td>
                    </tr>
                    <tr>
                        <td style="padding: 5px 0; color: #64748b;">E-mail:</td>
                        <td style="padding: 5px 0;">{form['email']}</td>
                    </tr>
                    <tr>
                        <td style="padding: 5px 0; color: #64748b;">Contato:</td>
                        <td style="padding: 5px 0;">{form['contato']}</td>
                    </tr>
                </table>
    
                <h2 style="font-size: 16px; color: #334155; border-left: 4px solid #2563eb;
                padding-left: 10px; margin-bottom: 15px;">Detalhes da Solicitação</h2>
                <div style="background-color: #f8fafc; padding: 15px;
                border-radius: 6px; font-size: 14px; margin-bottom: 25px;">
                    <p style="margin: 0 0 10px;"><strong>Assunto:</strong> {form['assunto']}</p>
                    <p style="margin: 0 0 10px;"><strong>Nota Fiscal:</strong> {form['nota_fiscal']}</p>
                    <p style="margin: 0 0 5px;"><strong>Tipo de Problema:</strong> {form['problema']}</p>
                    <p style="margin: 10px 0 0; color: #475569; line-height: 1.5;"><strong>
                    Descrição:</strong><br>{form['descricao']}</p>
                </div>
    
                <h2 style="font-size: 16px; color: #334155;
                border-left: 4px solid #2563eb; padding-left: 10px; margin-bottom: 15px;">Itens para Devolução</h2>
                <table style="width: 100%; font-size: 13px; border-collapse: collapse;
                border: 1px solid #e2e8f0;">
                    <thead>
                        <tr style="background-color: #f1f5f9; text-align: left;">
                            <th style="padding: 10px; border: 1px solid #e2e8f0;">Produto / ID</th>
                            <th style="padding: 10px; border: 1px solid #e2e8f0;">Qtd. Original</th>
                            <th style="padding: 10px; border: 1px solid #e2e8f0;">Qtd. Devolução</th>
                        </tr>
                    </thead>
                    <tbody>
                        {''.join([
                            f"""<tr>
                                <td style="padding: 10px; border: 1px solid #e2e8f0;">
                                {item['nome_produto']} <br><small style="color:#64748b;">ID: {item['id']}</small></td>
                                <td style="padding: 10px; border: 1px solid #e2e8f0; text-align: center;">
                                {item['quantidade_original']}</td>
                                <td style="padding: 10px; border: 1px solid #e2e8f0;
                                text-align: center; font-weight: bold; color: #b91c1c;">
                                {item['quantidade_devolucao']}</td>
                            </tr>"""
                            for item in form["itens"]
                        ])}
                    </tbody>
                </table>
            </div>
    
            <div style="padding: 20px 30px; background-color: #f1f5f9;
            border-radius: 0 0 8px 8px; text-align: center;">
                <p style="font-size: 12px; color: #94a3b8; margin: 0;">
                    Este é um e-mail automático gerado pelo Sistema de Atendimento ao Cliente.
                    <br>Por favor, não responda a esta mensagem.
                </p>
            </div>
        </div>
    </body>
</html>
    """

    msg.set_content("Novo formulário SAC recebido")
    msg.add_alternative(html, subtype="html")

    # Anexo
    if caminho_arquivo:
        with open(caminho_arquivo, "rb") as f:
            conteudo = f.read()

        msg.add_attachment(
            conteudo,
            maintype="application",
            subtype="octet-stream",
            filename=os.path.basename(caminho_arquivo)
        )

    # Envio
    try:
        if not EMAIL_REMETENTE or not SENHA_APP:
            raise Exception("Credenciais de e-mail não configuradas")

        if "gmail.com" in EMAIL_REMETENTE:
            smtp_host = "smtp.gmail.com"
        elif "outlook.com" in EMAIL_REMETENTE or "hotmail.com" in EMAIL_REMETENTE:
            smtp_host = "smtp.office365.com"
        else:
            smtp_host = "smtp.hostinger.com"

        with smtplib.SMTP(smtp_host, 587) as smtp:
            smtp.starttls()
            smtp.login(EMAIL_REMETENTE, SENHA_APP)
            smtp.send_message(msg)
        
        print("EMAIL ENVIADO COM SUCESSO PARA O SAC! 🚀")

    except Exception as e:
        print(f"Erro ao enviar e-mail: {e}")