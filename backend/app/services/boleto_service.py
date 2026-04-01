import re
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import Table, TableStyle
from fastapi import HTTPException

import re
from io import BytesIO
from fastapi import HTTPException
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
# Importações necessárias para criar tabelas formais
from reportlab.platypus import Table, TableStyle

def validar_e_extrair(codigo_de_barras: str):
    linha = re.sub(r'\D', '', str(codigo_de_barras))
    if len(linha) < 40:
        raise HTTPException(status_code=400, detail="Linha digitável inválida.")
    
    bancos = {"341": "Itaú", "237": "Bradesco", "001": "Brasil", "033": "Santander", "104": "Caixa"}
    codigo_banco = linha[:3]
    nome_banco = bancos.get(codigo_banco, f"Banco {codigo_banco}")
            
    return {
        "banco_nome": nome_banco,
        "banco_codigo": codigo_banco,
        "linha_limpa": linha
    }

def gerar_pdf_bytes(boleto_db):
    info = validar_e_extrair(boleto_db.codigo_de_barras)
    
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=A4)
    largura_a4, altura_a4 = A4

    # --- FUNÇÕES AUXILIARES DE FORMATAÇÃO ---
    def formatar_data(dt):
        if dt and hasattr(dt, 'strftime'):
            return dt.strftime('%d/%m/%Y')
        return str(dt) if dt else "N/A"

    def formatar_moeda(valor):
        return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

    # --- 1. CABEÇALHO FORMAL (Identificação do Banco) ---
    y = altura_a4 - 50 # Ponto de partida no topo
    
    # Linha grossa superior
    c.setLineWidth(2)
    c.line(40, y, 555, y)
    
    y -= 25
    c.setFont("Helvetica-Bold", 14)
    # Ex: ITAÚ | 341-9
    c.drawString(45, y, f"{info['banco_nome'].upper()}  |  {info['banco_codigo']}-9")
    
    # Fonte monoespaçada para a Linha Digitável (facilita leitura)
    c.setFont("Courier-Bold", 11)
    # Alinhado à direita
    c.drawRightString(550, y, info['linha_limpa'])
    
    y -= 5
    c.setLineWidth(1)
    c.line(40, y, 555, y)

    y -= 15
    
    venc_str = formatar_data(boleto_db.vencimento)
    criado_str = formatar_data(boleto_db.criado_em)
    valor_str = formatar_moeda(boleto_db.valor_total)
    
    dados_tabela = [
        
        ["Beneficiário", "", "Vencimento"],
        ["LAFMED DISTRIBUIDORA FARMACEUTICA LTDA\nCNPJ: 34.588.023/0001-80", "", venc_str],
        ["Pagador (CNPJ)", "Data Emissão", "Valor do Documento"],
        [f"{boleto_db.cnpj}", criado_str, valor_str]
    ]
    
    tabela = Table(dados_tabela, colWidths=[250, 115, 150])
    
    estilo_tabela = TableStyle([
        ('FONT', (0, 0), (-1, 0), 'Helvetica-Bold', 8), 
        ('FONT', (0, 2), (-1, 2), 'Helvetica-Bold', 8),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
        ('TEXTCOLOR', (0, 2), (-1, 2), colors.black),
        ('VALIGN', (0, 0), (-1, 0), 'BOTTOM'),
        ('VALIGN', (0, 2), (-1, 2), 'BOTTOM'),
        ('FONT', (0, 1), (-1, 1), 'Helvetica', 10),
        ('FONT', (0, 3), (-1, 3), 'Helvetica-Bold', 11), 
        ('VALIGN', (0, 1), (-1, 1), 'TOP'),
        ('VALIGN', (0, 3), (-1, 3), 'TOP'),

        ('SPAN', (0, 0), (1, 0)), 
        ('SPAN', (0, 1), (1, 1)),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
        ('ALIGN', (2, 0), (2, -1), 'RIGHT'), 
        ('ALIGN', (1, 2), (1, 3), 'RIGHT'), 
    ])
    
    tabela.setStyle(estilo_tabela)
    

    tabela.wrapOn(c, 40, y)
    tabela.drawOn(c, 40, y - 80) # Ajuste a coordenada Y para baixo baseada na altura da tabela

    y -= 110 # Pula a área da tabela
    
    # Linha divisória
    c.setDash(1, 2) # Linha pontilhada
    c.line(40, y, 555, y)
    c.setDash() # Restaura linha sólida

    y -= 20
    c.setFont("Helvetica-Bold", 10)
    c.drawString(45, y, "Instruções para o Cliente Lafmed:")
    
    c.setFont("Helvetica", 9)
    y -= 15
    instrucoes = [
        "1. Este documento é apenas uma representação visual para conferência de dados.",
        "2. NÃO utilize este impresso para pagamento em guichês de caixa ou lotéricas.",
        "3. Utilize a LINHA DIGITÁVEL (código numérico) no topo deste documento no seu Internet Banking ou App.",
        "4. Confirme se o Beneficiário é LAFMED DISTRIBUIDORA antes de finalizar o pagamento."
    ]
    
    for linha in instrucoes:
        c.drawString(55, y, linha)
        y -= 12

    c.saveState() 
    c.setFont("Helvetica-Bold", 50)
    c.setFillColor(colors.Color(0.9, 0.9, 0.9, alpha=0.5)) 
    c.translate(largura_a4/2, altura_a4/2) 
    c.rotate(45) 
    c.drawCentredString(0, 0, "NÃO SERVE COMO")
    c.drawCentredString(0, -55, "DOCUMENTO OFICIAL")
    c.restoreState() 

    # Finaliza a página
    c.showPage()
    c.save()
    
    buffer.seek(0)
    return buffer