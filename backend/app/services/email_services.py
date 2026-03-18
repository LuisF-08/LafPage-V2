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
    msg.set_content(f"Seu código de verificação é: {codigo}")

    with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
        smtp.starttls()
        smtp.login(EMAIL_REMETENTE, SENHA_APP)
        smtp.send_message(msg)

    print("EMAIL ENVIADO!")

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