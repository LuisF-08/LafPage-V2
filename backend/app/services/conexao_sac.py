import psycopg2
import os
from dotenv import load_dotenv
from psycopg2.extras import RealDictCursor

load_dotenv()
HOST = os.getenv("DB_HOST")
BANCO = os.getenv("DB_DATABASE")
USUARIO= os.getenv("DB_USER")
SENHA = os.getenv("DB_PASSWORD")
PORTA = os.getenv("DB_PORT", "5432")


def get_conexao_banco():
    return psycopg2.connect(host=HOST,
                            database=BANCO,
                            user=USUARIO,
                            password=SENHA,
                            port=PORTA)


def validar_cnpj_banco(cnpj):
    conexao = get_conexao_banco()
    try:
        cursor = conexao.cursor()
        
        # DEBUG
        cursor.execute("SELECT current_database(), inet_server_port();")
        db_info = cursor.fetchone()
        print(f"\n--- DEBUG CONEXÃO ---")
        print(f"Banco: {db_info[0]} | Porta: {db_info[1]}")
        
        cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'")
        tabelas = [t[0] for t in cursor.fetchall()]
        print(f"Tabelas que o Python enxerga: {tabelas}")
        print(f"----------------------\n")
        
        # Execução da query principal
        cursor.execute("SELECT cnpj FROM clientes WHERE cnpj = %s", (cnpj,))
        resultado = cursor.fetchone()
        
        if resultado:
            return {"existe": True, "cnpj": resultado[0]}
        else:
            return {"existe": False, "mensagem": f"O {cnpj} não foi encontrado"}
            
    except Exception as e:
        print(f"ERRO NA CONSULTA: {e}")
        raise e
    finally:
        cursor.close()
        conexao.close()
    
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
    
    