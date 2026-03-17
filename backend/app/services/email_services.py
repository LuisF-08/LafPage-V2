import random
import time

codigos = {}

async def enviar_email_codigo(email):
    codigo = str(random.randint(100000, 999999))

    codigos[email] = {
        "codigo": codigo,
        "expira": time.time() + 300
    }

    print(f"Código enviado para {email}: {codigo}")  # simulação

    return {"ok": True}

def validar_codigo(email, codigo):
    registro = codigos.get(email)

    if not registro:
        return {"valido": False}

    if time.time() > registro["expira"]:
        return {"valido": False}

    if registro["codigo"] != codigo:
        return {"valido": False}

    del codigos[email]

    return {"valido": True}