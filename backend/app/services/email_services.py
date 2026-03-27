import time, secrets, smtplib
from email.message import EmailMessage
from email_validator import EmailNotValidError, validate_email
import os
from dotenv import load_dotenv

load_dotenv()
EMAIL_REMETENTE = os.getenv("EMAIL_USER")
SENHA_APP = os.getenv("EMAIL_PASS")

codigos = {}


def enviar_email_real(email, codigo):
    msg = EmailMessage()
    msg["Subject"] = "CÓDIGO DE VERIFICAÇÃO"
    msg["From"] = EMAIL_REMETENTE
    msg["To"] = email

    #   acessibilidade e anti-spam
    msg.set_content(f"Seu código de verificação é: {codigo}")

    # Conteúdo em html que vai ao email
    html_content = f"""
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
    </head>
    <body style="margin: 0; padding: 0; background-color: #f4f7f6; 
    font-family: Arial, sans-serif;">
        <table width="100%" cellpadding="0" cellspacing="0" border="0" 
        style="background-color: #f4f7f6; padding: 40px 0;">
            <tr>
                <td align="center">
                    <table width="600" cellpadding="0" cellspacing="0" border="0"
                      style="background-color: #ffffff; border-radius: 8px; box-shadow:
                        0 4px 10px rgba(0,0,0,0.1); overflow: hidden;">
                        
                        <tr>
                            <td style="background-color: #4A90E2; padding: 30px;
                              text-align: center;">
                                <h1 style="color: #ffffff; margin: 0; font-size:
                                  24px; font-weight: normal;">Verificação de Segurança</h1>
                            </td>
                        </tr>
                        
                        <tr>
                            <td style="padding: 40px 30px; text-align: center;">
                                <p style="color: #333333; font-size: 16px; 
                                line-height: 1.6; margin-top: 0;">
                                    Olá!<br>
                                    Recebemos uma solicitação para acessar sua conta. 
                                    Use o código abaixo para continuar:
                                </p>
                                
                                <div style="margin: 30px auto; background-color: #f8f9fa;
                                  border: 2px dashed #4A90E2; border-radius: 8px; padding: 20px; width: 60%; text-align: center;">
                                    <span style="font-size: 32px; font-weight: bold; color: 
                                    #4A90E2; letter-spacing: 5px;">{codigo}</span>
                                </div>
                                
                                <p style="color: #777777; font-size: 14px; line-height: 1.5; 
                                margin-bottom: 0;">
                                    O código é válido por tempo limitado.<br>
                                    Se você não solicitou este código,
                                      pode ignorar este e-mail com segurança.
                                </p>
                            </td>
                        </tr>
                        
                        <tr>
                            <td style="background-color: #f8f9fa; padding: 20px;
                              text-align: center; border-top: 1px solid #eeeeee;">
                                <p style="color: #aaaaaa; font-size: 12px; margin: 0;">
                                    Enviado automaticamente por nosso sistema.
                                      Por favor, não responda.
                                </p>
                            </td>
                        </tr>
                        
                    </table>
                </td>
            </tr>
        </table>
    </body>
    </html>
    """

    # Adiciona a versão em HTML à mensagem
    msg.add_alternative(html_content, subtype='html')
    try:
        if "gmail.com" in EMAIL_REMETENTE:
            smtp_host = "smtp.gmail.com"
            smtp_port = 587
        elif "outlook.com" in EMAIL_REMETENTE or "hotmail.com" in EMAIL_REMETENTE:
            smtp_host = "smtp.office365.com"
            smtp_port = 587
        else:
            smtp_host = "smtp.hostinger.com"
            smtp_port = 587

        with smtplib.SMTP(smtp_host, smtp_port) as smtp:
            smtp.starttls()
            smtp.login(EMAIL_REMETENTE, SENHA_APP)
            smtp.send_message(msg)
        print("EMAIL ENVIADO COM SUCESSO! 🚀")
    except Exception as e:
        print(f"Erro ao enviar e-mail: {e}")

async def enviar_email_codigo(email):
    try:
        valido = validate_email(email)
        print(f"Email válido: {valido.email}")
        print("EMAIL:", EMAIL_REMETENTE)
        print("SENHA:", SENHA_APP)
    except EmailNotValidError as e:
        return {"ok": False, "erro": str(e)}

    codigo = str(secrets.randbelow(900000) + 100000)

    codigos[email] = {
        "codigo": codigo,
        "expira": time.time() + 300
    }
    enviar_email_real(email, codigo)

    return {"ok": True}


def validar_codigo(email, codigo):
    try:
        valido = validate_email(email)
        print(f"Email válido: {valido.email}")
    except EmailNotValidError as e:
        return {"valido": False}

    registro = codigos.get(email)

    if not registro:
        return {"valido": False}

    if time.time() > registro["expira"]:
        return {"valido": False}

    if registro["codigo"] != codigo:
        return {"valido": False}

    del codigos[email]

    return {"valido": True}