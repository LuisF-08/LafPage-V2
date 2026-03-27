import psycopg2
import os
from dotenv import load_dotenv
from psycopg2.extras import RealDictCursor

load_dotenv()
HOST = os.getenv("DB_HOST")
BANCO = os.getenv("DB_DATABASE")
USUARIO= os.getenv("DB_USER")
SENHA = os.getenv("DB_PASSWORD")

def get_conexao_banco():
    return psycopg2.connect(host=HOST,
                            database=BANCO,
                            user=USUARIO,
                            password=SENHA)

def listar_sac():
    conn = get_conexao_banco()  
    cursor = conn.cursor()

    cursor.execute("""
        SELECT 
            c.nome,
            c.email,
            p.numero_pedido,
            s.descricao_problema,
            s.situacao,
            d.resposta,
            d.status
        FROM sac s
        JOIN pedidos p ON s.pedido_id = p.id
        JOIN clientes c ON p.id_cliente = c.id
        LEFT JOIN devolucao_sac d ON d.solicitacao_id = s.id;
    """)

    dados = cursor.fetchall()

    resultado = []
    for row in dados:
        resultado.append({
            "nome": row[0],
            "email": row[1],
            "pedido": row[2],
            "problema": row[3],
            "situacao": row[4],
            "resposta": row[5] or "",
            "status": row[6] or "",
        })

    cursor.close()
    conn.close()
    
    return resultado

def validar_cnpj_banco(cnpj):
    conexao = get_conexao_banco()
    cursor = conexao.cursor()
    
    cursor.execute(""" 
    SELECT cnpj FROM clientes
    WHERE cnpj = %s               
    """, (cnpj,))
    
    resultado = cursor.fetchone()
    
    cursor.close()
    conexao.close()
    
    if resultado :
        return {"existe": True , "cnpj": resultado[0] }
    else:
        return { "existe": True , "mensagem": f"O {cnpj} procurado não foi encontrado" }
    
def validar_nota_fiscal_banco(nota_fiscal):
    conexao = get_conexao_banco()
    cursor = conexao.cursor(cursor_factory=RealDictCursor)

    # verifica se existe
    cursor.execute("""
        SELECT * FROM pedidos
        WHERE nota_fiscal = %s
    """, (nota_fiscal,))
    
    pedido = cursor.fetchone()

    if not pedido:
        cursor.close()
        conexao.close()
        return {"existe": False}

    cursor.execute("""
        SELECT id,
        nome_produto,
        codigo_produto,
        nota_fiscal,
        valor_total,
        quantidade,
        solicitado 
        FROM pedidos
        WHERE nota_fiscal = %s
    """, (nota_fiscal,))

    itens = cursor.fetchall()

    cursor.close()
    conexao.close()

    return {
        "existe": True,
        "pedido": pedido,
        "itens": itens
    }
    
    