from validate_docbr import CNPJ

cnpj = CNPJ()

async def validar_cnpj(cnpj_recebido):
    cnpj_limpo = ''.join(filter(str.isdigit, cnpj_recebido))

    if not cnpj.validate(cnpj_limpo):
        return { "ok": False, "erro": "CNPJ inválido"}

    return { "ok": True,"cnpj": cnpj_limpo}
    